import os
import telegram
from telegram.ext import Updater, MessageHandler, Filters
import openai

# Inisialisasi bot Telegram
bot = telegram.Bot(token=os.environ.get('6231194913:AAHAKMup6rVe_c64kGZxmiAGO8qfQ2eHXs0'))

# Inisialisasi OpenAI API
openai.api_key = os.environ.get('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')

# Fungsi untuk menangani pesan yang diterima oleh bot
def handle_message(update, context):
    # Ambil pesan dari pengguna
    user_message = update.message.text

    # Kirim pesan ke OpenAI API
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_message,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Ambil jawaban dari OpenAI API
    bot_message = response.choices[0].text

    # Kirim jawaban ke pengguna
    update.message.reply_text(bot_message)

# Buat objek Updater dan jadwalkan pengambilan pesan secara berkala
updater = Updater(token=os.environ.get('TELEGRAM_TOKEN'), use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
updater.start_polling()

# Tampilkan pesan jika bot berjalan
print("Bot berjalan...")
