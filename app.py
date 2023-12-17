from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import json
import random

import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('TOKEN')

print("Bot is running...")

with open('./quotes.json', 'r') as file:
    data = json.load(file)

async def randomquote(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    datadict =(data[random.randint(0,(len(data)-1))])
    quote = datadict["quote"]
    author = datadict["author"]
    text = f"{quote}\n\nAuthor: {author}"
    await update.message.reply_text(text)

async def sryText(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = "Sorry I can't understand that command. Please type /help to get all the commands available."
    await update.message.reply_text(text)

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = "/help - list all the commands \n/random - get a random quote"
    await update.message.reply_text(text)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), sryText))
app.add_handler(CommandHandler("random", randomquote))
app.add_handler(CommandHandler("help", help))

app.run_polling()
