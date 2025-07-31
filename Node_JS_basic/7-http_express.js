// 7-http_express.js
const express = require('express');
const fs = require('fs');

const app = express();
const database = process.argv[2]; // Get database path from command line

// Function to read and process students from CSV file
function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.trim().split('\n').filter((line) => line);
      const students = lines.slice(1); // skip header
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
      let output = `Number of students: ${total}`;
      for (const field in fields) {
        if (Object.prototype.hasOwnProperty.call(fields, field)) {
          const list = fields[field];
          output += `\nNumber of students in ${field}: ${list.length}. List: ${list.join(', ')}`;
        }
      }

      resolve(output);
    });
  });
}

// Route: /
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Route: /students
app.get('/students', async (req, res) => {
  try {
    const report = await countStudents(database);
    res.type('text/plain').send(`This is the list of our students\n${report}`);
  } catch (error) {
    res.status(500).type('text/plain').send(`This is the list of our students\n${error.message}`);
  }
});

// Start server
app.listen(1245);

module.exports = app;
