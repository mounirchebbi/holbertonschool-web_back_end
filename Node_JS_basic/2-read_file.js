// 2-read_file.js
const fs = require('fs');

function countStudents(path) {
  try {
    // Read file content synchronously
    const data = fs.readFileSync(path, 'utf8');

    // Split lines and filter out empty ones
    const lines = data.trim().split('\n').filter(line => line);

    // Remove header
    const students = lines.slice(1);

    // Total student count
    console.log(`Number of students: ${students.length}`);

    const fields = {};

    // Group students by field
    for (const line of students) {
      const parts = line.split(',');
      const firstName = parts[0];
      const field = parts[3];

      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstName);
    }

    // Log per-field data
    for (const field in fields) {
      const list = fields[field];
      console.log(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
    }
  } catch (err) {
    // Handle file errors
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
