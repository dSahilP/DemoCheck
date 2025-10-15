const { exec } = require('child_process');

const user = process.argv[2] || '';
exec(user, (err, stdout, stderr) => {
  if (err) console.error(err);
  else console.log(stdout);
}); // 🚨 Command injection if user is untrusted
