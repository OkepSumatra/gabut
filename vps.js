const TelegramBot = require('node-telegram-bot-api');
const { NodeSSH } = require('node-ssh');

// Inisialisasi bot Telegram
const bot = new TelegramBot('BOT_TOKEN', { polling: true });

// Mendefinisikan fungsi untuk mengirim perintah SSH ke VPS
const sendCommandToVps = async (command) => {
  const ssh = new NodeSSH();
  await ssh.connect({
    host: 'VPS_IP_ADDRESS',
    username: 'VPS_USERNAME',
    password: 'VPS_PASSWORD'
  });
  const result = await ssh.execCommand(command);
  ssh.dispose();
  return result.stdout;
};

// Mendefinisikan handler perintah dari pengguna
bot.on('message', async (msg) => {
  const chatId = msg.chat.id;
  const command = msg.text;
  const result = await sendCommandToVps(command);
  bot.sendMessage(chatId, result);
});
