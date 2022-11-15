module.exports = {
  apps: [
    {
      name: "SelfBot",
      script: "./main.py",
      instances: 1,
      autorestart: true,
      watch: false,
      max_memory_restart: "1G",
      env: {
        NODE_ENV: "development",
        ...process.env,
      },
    },
  ],
};
