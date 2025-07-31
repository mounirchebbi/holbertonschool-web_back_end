// welcome message
process.stdout.write('Welcome to Holberton School, what is your name?\n');

// Set up  event listener
process.stdin.on('readable', () => {
  const name = process.stdin.read();

  if (name) {
    process.stdout.write(`Your name is: ${name}`);
  }
});

// Set up 'end' event listener
process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});

process.stdin.resume();
