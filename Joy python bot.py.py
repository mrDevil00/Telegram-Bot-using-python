from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes,filters

TOKEN: Final = '6985163788:AAEmAOaS_DDbrZeqTkcFt1DGznRwaciLNko'

BOT_USERNAME: Final = '@Joy_python_bot'


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Hello! Thanks for chatting with me! I am a Python_Bot!""")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Hello! This is help command! How can i help!
If you are facing any problem or having problem related to Bot then you can mail on xyz987@gmail.com.""")


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""This is a custom command!
    Here are some predefined commands that can be answered by Python_Bot.
    1.What is python?
    2.Comment in python?
    3.Variables in python?
    4.Data types in python?
    5.Functions in python?
    6.Name some libraries of python?
    7.Exception handling in python?
    8.File handling in python?""")



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
    
    if 'what is python?' in processed:
        return ' Python is a high-level programming language known for its simplicity and readability. Its versatile, used in web development, data analysis, artificial intelligence, and more.'  
    
    if 'comment in python?' in processed:
        return """for multiple line (""" """ or ''' ''') and '#' for single line comment."""
        
    if 'data types in python?' in processed:
        return "Python has several data types including int for integers, float for floating-point numbers, str for strings, bool for Boolean values, list, tuple, and dict for data structures, among others."
        
    if 'variables in python?' in processed:
        return """You can declare a variable in Python by assigning a value to a name.
        Like x=5,abc1=10, etc. But never start a variable name with digit.
        We can start a variable name with _ , a1 , a not like 12a. """
        
    if 'functions in python?' in processed:
        return """By using 'def' keyword we can create function.
        There are two types of functions in python 1. Built in function and 2. User define function.
        Built in function:- The functions which are coming along with Python software automatically, are called built in functions or predefined functionsExample: id() , type() , input() , eval() , etc..
        User define function:- The functions which are developed by programmer explicitly according to business requirements, are called user defined functions.
        Syntax to create user defined functions:
        Like this- def function_name(parameters):"""
        
    if 'name some libraries of python?' in processed:
        return """A Python library is a collection of functions and methods that allow you to perform many actions without writing your own code.
        Some of the python libraries are Pandas, Numpy, turtle, time and many more."""
    
    if 'exception handling in python?' in processed:
        return """Exceptions in Python can be handled using try, except, and optionally 'finally' blocks. For example
            try:
            # code that might raise an exception
            result = 10 / 0
            except ZeroDivisionError:
            print("Cannot divide by zero!")
            """
        
    if 'file handling in python?' in processed:
        return """ You can open a file using the open() function, read or write content, and close the file using close(). For instance:
            file = open('example.txt', 'r')  # 'r' for reading, 'w' for writing
              content = file.read()  # read file content
              file.close()  # close the file
              """
        
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