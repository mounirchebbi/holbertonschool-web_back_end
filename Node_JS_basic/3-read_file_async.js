// 3-read_file_async.js
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    // Read file asynchronously
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        // Reject promise with error
        reject(new Error('Cannot load the database'));
        return;
      }

      // Split lines and remove empty ones
      const lines = data.trim().split('\n').filter((line) => line);

      // Remove header
      const students = lines.slice(1);

      // Total number of students
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

      // Display each field's stats
      for (const field in fields) {
        if (Object.prototype.hasOwnProperty.call(fields, field)) {
          const list = fields[field];
          console.log(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
        }
      }

      resolve(); // Resolve promise on success
    });
  });
}

module.exports = countStudents;
