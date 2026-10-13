#!/usr/bin/env node
import { makeWASocket, useMultiFileAuthState, DisconnectReason } from '@whiskeysockets/baileys';
import pino from 'pino';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const AUTH_DIR = path.join(__dirname, 'auth_info');
const GROUP_JID = '120363425211205411@g.us'; // Distribuidores Stream Zone 🔥
const DEFAULT_OFFICIAL_PHONE = '573114668309'; // Stream Zone Oficial

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

// Parse CLI arguments
const argv = process.argv.slice(2);
let tasksFile = fs.existsSync('/tmp/consolidated_notifications.json')
    ? '/tmp/consolidated_notifications.json'
    : '/tmp/pending_notifications.json';
let metaFile = '/tmp/sz_last_report.json';
let excelPath = null;
let officialPhone = DEFAULT_OFFICIAL_PHONE;
let noOfficial = false;
let delayMs = 5000;
let noGroup = false;
let dryRun = false;
let limit = null;

for (let i = 0; i < argv.length; i++) {
    if (argv[i] === '--file' && argv[i + 1]) {
        tasksFile = argv[++i];
    } else if (argv[i] === '--meta' && argv[i + 1]) {
        metaFile = argv[++i];
    } else if (argv[i] === '--excel' && argv[i + 1]) {
        excelPath = argv[++i];
    } else if (argv[i] === '--official' && argv[i + 1]) {
        officialPhone = argv[++i].replace(/[^0-9]/g, '');
    } else if (argv[i] === '--no-official') {
        noOfficial = true;
    } else if (argv[i] === '--delay' && argv[i + 1]) {
        delayMs = Math.round(parseFloat(argv[++i]) * 1000);
    } else if (argv[i] === '--no-group') {
        noGroup = true;
    } else if (argv[i] === '--dry-run') {
        dryRun = true;
    } else if (argv[i] === '--limit' && argv[i + 1]) {
        limit = parseInt(argv[++i], 10);
    }
}

// Cargar metadata si existe
let meta = {};
if (fs.existsSync(metaFile)) {
    try {
        meta = JSON.parse(fs.readFileSync(metaFile, 'utf-8'));
        if (!excelPath && meta.excel_path) {
            excelPath = meta.excel_path;
        }
    } catch (e) {}
}

async function main() {
    if (!fs.existsSync(tasksFile)) {
        console.error(`❌ No se encontró el archivo de tareas en ${tasksFile}`);
        process.exit(1);
    }

    let tasks = JSON.parse(fs.readFileSync(tasksFile, 'utf-8'));
    if (limit && limit > 0) {
        tasks = tasks.slice(0, limit);
    }

    const totalRecords = meta.total_records || tasks.length;
    const startStr = meta.start_str || 'Hoy';
    const endStr = meta.end_str || 'Próximos 4 días';

    console.log(`📋 Total de clientes a notificar: ${tasks.length}`);
    console.log(`📈 Total de suscripciones en corte: ${totalRecords}`);
    console.log(`⏱️ Intervalo anti-spam: ${delayMs / 1000}s`);

    const officialCaption = (
        `📊 *REPORTE OFICIAL DE VENCIMIENTOS (STREAM ZONE)*\n\n` +
        `📅 *Rango de corte*: ${startStr} al ${endStr} (0 a 4 días)\n` +
        `📈 *Total suscripciones en corte*: ${totalRecords}\n` +
        `👥 *Clientes únicos a notificar*: ${tasks.length}\n\n` +
        `📌 Adjunto el archivo Excel corporativo con el desglose oficial de 13 columnas, credenciales completas (correo, contraseña, perfil, PIN) y estados de cobro actualizados.\n\n` +
        `⚡ Despachando notificaciones automáticas a clientes con retardo anti-spam de ${delayMs / 1000}s...`
    );

    if (dryRun) {
        console.log(`\n🔍 MODO SIMULACIÓN (DRY-RUN) - No se enviará ningún mensaje real:\n`);
        if (excelPath && !noOfficial) {
            console.log(`[1/3] 📊 PREVIEW REPORTE OFICIAL STREAM ZONE (+${officialPhone}):`);
            console.log(`   Archivo: ${excelPath}`);
            console.log(`   Caption:\n   ` + officialCaption.replace(/\n/g, '\n   '));
            console.log('----------------------------------------------------');
        }
        console.log(`[2/3] 👥 PREVIEW NOTIFICACIONES A CLIENTES (${tasks.length} clientes):`);
        tasks.forEach((t, idx) => {
            console.log(`[${idx + 1}/${tasks.length}] 📱 +${t.phone} | 👤 ${t.name} | 🧾 ${t.order}`);
            console.log(`   Mensaje preview:\n   ` + t.message.replace(/\n/g, '\n   '));
            console.log('----------------------------------------------------');
        });
        if (!noGroup) {
            console.log(`[3/3] 📢 PREVIEW AVISO A GRUPO DISTRIBUIDORES: ACTIVO (después del lote)`);
        }
        process.exit(0);
    }

    const { state, saveCreds } = await useMultiFileAuthState(AUTH_DIR);
    const sock = makeWASocket({
        auth: state,
        logger: pino({ level: 'silent' }),
        printQRInTerminal: false
    });

    sock.ev.on('creds.update', saveCreds);

    sock.ev.on('connection.update', async (update) => {
        const { connection, lastDisconnect } = update;

        if (connection === 'connecting') {
            console.log('🟡 Conectando con WhatsApp...');
        } else if (connection === 'close') {
            const statusCode = lastDisconnect?.error?.output?.statusCode;
            if (statusCode === DisconnectReason.loggedOut) {
                console.error('❌ Sesión cerrada o desvinculada.');
                process.exit(1);
            }
        } else if (connection === 'open') {
            console.log(`🟢 Conexión activa como: ${sock.user?.name || 'Stream Zone'} (${sock.user?.id})`);

            // PASO 1: Enviar Reporte Excel a Stream Zone Oficial
            if (excelPath && fs.existsSync(excelPath) && !noOfficial) {
                console.log(`\n📤 [1/3] Enviando reporte Excel a Stream Zone Oficial (+${officialPhone})...`);
                try {
                    const excelBuffer = fs.readFileSync(excelPath);
                    await sock.sendMessage(`${officialPhone}@s.whatsapp.net`, {
                        document: excelBuffer,
                        fileName: path.basename(excelPath),
                        mimetype: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                        caption: officialCaption
                    });
                    console.log(`  ✅ Reporte Excel entregado a Stream Zone Oficial.`);
                    console.log(`  ⏳ Esperando ${delayMs / 1000}s anti-spam antes de clientes...`);
                    await sleep(delayMs);
                } catch (err) {
                    console.error(`  ⚠️ Error al enviar reporte a Stream Zone Oficial:`, err.message);
                }
            } else if (!excelPath) {
                console.log(`\nℹ️ [1/3] No se especificó reporte Excel para Stream Zone Oficial, omitiendo.`);
            }

            // PASO 2: Despacho secuencial a clientes con delay anti-spam
            console.log(`\n🚀 [2/3] Iniciando despacho secuencial a clientes con retardo de ${delayMs / 1000}s...\n`);
            let sentCount = 0;
            let errorCount = 0;

            for (let i = 0; i < tasks.length; i++) {
                const t = tasks[i];
                const jid = `${t.phone}@s.whatsapp.net`;
                console.log(`[${i + 1}/${tasks.length}] 📤 Enviando a ${t.name} (+${t.phone}) - Orden: ${t.order}...`);
                
                try {
                    await sock.sendMessage(jid, { text: t.message });
                    console.log(`  ✅ Entregado a ${t.name}`);
                    sentCount++;
                } catch (err) {
                    console.error(`  ⚠️ Error al enviar a ${t.name} (+${t.phone}):`, err.message);
                    errorCount++;
                }

                if (i < tasks.length - 1) {
                    console.log(`  ⏳ Esperando ${delayMs / 1000}s anti-spam...`);
                    await sleep(delayMs);
                }
            }

            console.log(`\n🎉 Despacho a clientes completado: ${sentCount} exitosos, ${errorCount} fallidos.`);

            // PASO 3: Aviso final al grupo de distribuidores
            if (!noGroup) {
                console.log(`\n⏳ Esperando 5 segundos antes de avisar al grupo de distribuidores...`);
                await sleep(5000);

                const groupMsg = (
                    "¡Hola a todos! 🙌\n\n" +
                    "Les informamos que ya se enviaron las notificaciones de los vencimientos y fechas de corte próximas a cada uno de los clientes.\n\n" +
                    "Quedamos muy atentos y esperamos su pronta respuesta para renovar los accesos sin interrupciones.\n\n" +
                    "¡Muchas bendiciones a todos! ✨🙏"
                );

                console.log(`📢 [3/3] Enviando reporte al grupo 'Distribuidores Stream Zone 🔥'...`);
                try {
                    await sock.sendMessage(GROUP_JID, { text: groupMsg });
                    console.log(`✅ Confirmación enviada exitosamente al grupo de distribuidores.`);
                } catch (err) {
                    console.error(`⚠️ Error al enviar al grupo:`, err.message);
                }
            }

            console.log(`\n🏁 Proceso de vencimientos finalizado al 100%.`);
            await sleep(3000);
            try { sock.end(); } catch (e) {}
            process.exit(0);
        }
    });
}

main().catch((err) => {
    console.error("Fallo general:", err);
    process.exit(1);
});
