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

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

// Parse CLI arguments
const argv = process.argv.slice(2);
let tasksFile = '/tmp/pending_notifications.json';
let delayMs = 5500;
let noGroup = false;
let dryRun = false;
let limit = null;

for (let i = 0; i < argv.length; i++) {
    if (argv[i] === '--file' && argv[i + 1]) {
        tasksFile = argv[++i];
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

async function main() {
    if (!fs.existsSync(tasksFile)) {
        console.error(`❌ No se encontró el archivo de tareas en ${tasksFile}`);
        process.exit(1);
    }

    let tasks = JSON.parse(fs.readFileSync(tasksFile, 'utf-8'));
    if (limit && limit > 0) {
        tasks = tasks.slice(0, limit);
    }

    console.log(`📋 Total de notificaciones a procesar: ${tasks.length}`);
    console.log(`⏱️ Intervalo anti-ban: ${delayMs / 1000}s`);

    if (dryRun) {
        console.log(`\n🔍 MODO SIMULACIÓN (DRY-RUN) - No se enviarán mensajes:\n`);
        tasks.forEach((t, idx) => {
            console.log(`[${idx + 1}/${tasks.length}] 📱 +${t.phone} | 👤 ${t.name} | 🧾 ${t.order}`);
            console.log(`   Mensaje preview:\n   ` + t.message.replace(/\n/g, '\n   '));
            console.log('----------------------------------------------------');
        });
        if (!noGroup) {
            console.log(`📢 Aviso final al grupo de distribuidores: ACTIVO (después del lote)`);
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
            console.log(`🚀 Iniciando despacho secuencial con retardo anti-ban...\n`);

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
                    console.log(`  ⏳ Esperando ${delayMs / 1000}s para evitar ban...`);
                    await sleep(delayMs);
                }
            }

            console.log(`\n🎉 Despacho individual completado: ${sentCount} exitosos, ${errorCount} fallidos.`);

            if (!noGroup) {
                console.log(`⏳ Esperando 5 segundos antes de avisar al grupo de distribuidores...`);
                await sleep(5000);

                const groupMsg = (
                    "¡Hola a todos! 🙌\n\n" +
                    "Les informamos que ya se enviaron las notificaciones de los vencimientos y fechas de corte próximas a cada uno de los clientes.\n\n" +
                    "Quedamos muy atentos y esperamos su pronta respuesta para renovar los accesos sin interrupciones.\n\n" +
                    "¡Muchas bendiciones a todos! ✨🙏"
                );

                console.log(`📢 Enviando reporte al grupo 'Distribuidores Stream Zone 🔥'...`);
                try {
                    await sock.sendMessage(GROUP_JID, { text: groupMsg });
                    console.log(`✅ Mensaje enviado exitosamente al grupo de distribuidores.`);
                } catch (err) {
                    console.error(`⚠️ Error al enviar al grupo:`, err.message);
                }
            }

            console.log(`\n🏁 Proceso de notificación finalizado al 100%.`);
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
