// 4-http.js
const http = require('http');

// Create HTTP server
const app = http.createServer((req, res) => {
  res.statusCode = 200; // OK
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello Holberton School!');
});

// Listen on port 1245
app.listen(1245);

module.exports = app;
