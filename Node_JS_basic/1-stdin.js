const readline = require('readline');

// Create readline interface to read from standard input and output
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Ask the question
rl.question('Welcome to Holberton School, what is your name?\n', (answer) => {
  console.log(`Your name is: ${answer}`);
  rl.close();
});

// When the input stream is closed
rl.on('close', () => {
  console.log('This important software is now closing');
});
