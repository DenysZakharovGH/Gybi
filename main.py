
import telebot
from googletrans import Translator
from telebot import types 

translator = Translator()

start_message= "let's start with Gybi. Write you words here:"
help_message= "Gybi here to help you translate words quickly\n any language ----> Ru \n  Ru/Uk ----> English \n"

bot = telebot.TeleBot("****************************************")

@bot.message_handler(commands=['start','help'])
def handle_start_help_message(message):
    if (message.text == "/start"):
        bot.send_message(message.chat.id,start_message)
    else:
        bot.send_message(message.chat.id,help_message)
      

@bot.message_handler(func=lambda message: True)
def translate_me_message(message):
    try:
        language = translator.detect(message.text).lang
        if(translator.detect(message.text).lang  not in ('ru uk')):
           message_request = message.text +"("+language+")"+" ----> (ru)" + translator.translate(message.text,'ru', language).text
        else:
           message_request = message.text  +"("+language+")"+" ---->  (en)" + translator.translate(message.text).text
        bot.send_message(message.chat.id, message_request)
    except Exception:
        bot.send_message(message.chat.id,"It's not a word. I'm confused" + u'\U0001F614' )


if __name__ == '__main__':
    bot.polling(none_stop = True)
