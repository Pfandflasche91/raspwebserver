const http = require('http');
const fs = require('fs');
const path = require('path');

const IP = '192.168.2.208'; // Deine IP-Adresse
const PORT = 3000; // Dein Port

// Erstelle einen HTTP-Server
const server = http.createServer((req, res) => {
  // Lese den Dateiinhalt der index.html-Datei
  fs.readFile(path.join(__dirname, 'website', 'index.html'), (err, data) => {
    if (err) {
      // Wenn ein Fehler beim Lesen der Datei auftritt, sende einen 500-Serverfehler zurück
      res.writeHead(500, {'Content-Type': 'text/plain'});
      res.end('500 - Internal Server Error');
    } else {
      // Wenn die Datei erfolgreich gelesen wurde, sende den Dateiinhalt zurück
      res.writeHead(200, {'Content-Type': 'text/html'});
      res.end(data);
    }
  });
});

// Starte den Server
server.listen(PORT, IP, () => {
  console.log(`Server läuft unter http://${IP}:${PORT}`);
});