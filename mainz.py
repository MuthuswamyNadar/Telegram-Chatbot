
import telebot

Token="7212935657:AAGoNcm9vYWMhaTnctil1dvMskt068QGu7E"

bot=telebot.TeleBot(Token)

@bot.message_handler(['start'])
def start(message):
    bot.reply_to(message,"Welcome to my club ")



@bot.message_handler(['help'])
def help(message):
    bot.reply_to(message,"""
        /start --> to run the start command
        /help --> to ask the help from bot
""")

@bot.message_handler()
def custom(message):
    try:
       msg=eval(message.text.strip())
    except Exception as e:
       msg="This can't be evaluated"
    bot.reply_to(message,msg)


bot.polling()























































