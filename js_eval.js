const user = process.argv[2] || 'console.log("safe")';
eval(user); // 🚨 eval of untrusted input
