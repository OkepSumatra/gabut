import telegram
import openai

# Setup OpenAI API
openai.api_key = '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'

# Setup Telegram Bot
bot = telegram.Bot(token='6231194913:AAHAKMup6rVe_c64kGZxmiAGO8qfQ2eHXs0')

# Function to respond to Telegram messages
def respond(bot, update):
    message = update.message.text
    # Call OpenAI's GPT-3 API to generate a response
    response = openai.Completion.create(
        engine='davinci',
        prompt=message,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5
    )
    bot.send_message(chat_id=update.message.chat_id, text=response.choices[0].text)

# Start Telegram bot
updater = telegram.ext.Updater(token='6231194913:AAHAKMup6rVe_c64kGZxmiAGO8qfQ2eHXs0')
updater.dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, respond))
updater.start_polling()
updater.idle()
