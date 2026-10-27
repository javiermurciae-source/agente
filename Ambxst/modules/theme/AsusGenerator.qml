import QtQuick
import Quickshell
import Quickshell.Io

QtObject {
    id: root

    function generate(Colors) {
        if (!Colors)
            return;

        const fmt = c => c ? c.toString().replace("#", "") : "";
        const primaryColor = fmt(Colors.primary);

        if (!primaryColor)
            return;

        writerProcess.command = ["asusctl", "aura", "effect", "static", "-c", primaryColor];
        writerProcess.running = true;
    }

    property Process writerProcess: Process {
        id: writerProcess
        running: false
        stdout: StdioCollector {
            onStreamFinished: console.log("AsusGenerator: Keyboard LED updated successfully.")
        }
        stderr: StdioCollector {
            onStreamFinished: err => {
                if (err)
                    console.error("AsusGenerator Error:", err);
            }
        }
    }
}
