from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes,filters

TOKEN: Final = 'TOKEN_NUMBER_OF_YOUR_BOT'

BOT_USERNAME: Final = 'BOT_USERNAME'


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Hello! Thanks for chatting with me! I am a Python_Bot!""")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Hello! This is help command! How can i help!
If you are facing any problem or having problem related to Bot then you can mail on xyz987@gmail.com.""")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""This is a custom command!
    """)



# responses

def handle_response(text: str) -> str:
    processed: str = text.lower()
    

    if "hello" in processed:
        return 'Hey there!'

    if 'how are you' in processed:
        return 'I am good!'

    if 'i love python' in processed:
        return 'I love too!'
    
    if 'i want to learn' in processed:
        return 'Great! lets start from basics.'
    
    if 'what is your name' in processed:
        return 'I am Joy! A python bot.'
    
    if 'who made you' in processed:
        return 'I am created as a project which includes many people.'
    
    if 'thank you' in processed:
        return 'Welcome! Feel free to ask anything.'
    
    if 'hi' in processed:
        return 'Hey there!'
    
    if 'i want to play games' in processed:
        return 'Sorry! We dont have games right now.'
    
    if 'bye' in processed:
        return 'Bye! Have a good day.'
    
  
    return "I do not understand what you wrote...."

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
        else:
            return
    else:
        response: str = handle_response(text)
    print('Bot:',  response)
    await update.message.reply_text(response)

    async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
        print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print("starting bot...")
    app = Application.builder().token(TOKEN).build()

    #commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    #messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))


    #polls the bot
    print("polling...")
    app.run_polling(poll_interval=3)