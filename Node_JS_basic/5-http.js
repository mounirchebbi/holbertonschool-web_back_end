// 5-http.js
const http = require('http');
const fs = require('fs');

// Get the database path from command-line arguments
const database = process.argv[2];

// Async function to read and process the database
function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.trim().split('\n').filter((line) => line);
      const students = lines.slice(1);
      const fields = {};

      for (const line of students) {
        const parts = line.split(',');
        const firstName = parts[0];
        const field = parts[3];

        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstName);
      }

      const total = students.length;
      let result = `Number of students: ${total}`;
      for (const field in fields) {
        if (Object.prototype.hasOwnProperty.call(fields, field)) {
          const names = fields[field].join(', ');
          result += `\nNumber of students in ${field}: ${fields[field].length}. List: ${names}`;
        }
      }

      resolve(result);
    });
  });
}

// Create HTTP server
const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    countStudents(database)
      .then((output) => {
        res.end(`This is the list of our students\n${output}`);
      })
      .catch((err) => {
        res.statusCode = 500;
        res.end('This is the list of our students\n' + err.message);
      });
  } else {
    res.statusCode = 404;
    res.end('Not found');
  }
});

// Start server on port 1245
app.listen(1245);

module.exports = app;
