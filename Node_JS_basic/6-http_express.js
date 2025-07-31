// 6-http_express.js
const express = require('express');

const app = express(); // Create Express app

// Route for root path
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Start server on port 1245
app.listen(1245);

module.exports = app; // Export app
