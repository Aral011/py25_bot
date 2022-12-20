import telebot
import random

from env import TOKEN

bot = telebot.TeleBot(TOKEN)

keyboard = telebot.types.ReplyKeyboardMarkup()
button1 = telebot.types.KeyboardButton('Да')
button2 = telebot.types.KeyboardButton('Нет')
keyboard.add(button1, button2)


@bot.message_handler(commands=['start', 'hi'])
def start_function(message):
    msg = bot.send_message(message.chat.id, f'Привет {message.chat.first_name} начнем игру?', reply_markup=keyboard)
    bot.register_next_step_handler(msg, answer_check)
    # bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJKU2OhPbZpzXetZeqfLyVz6z-5UcY_AAIVAAPANk8TzVamO2GeZOcsBA')
    # bot.send_photo(message.chat.id, 'https://media.proglib.io/wp-uploads/2018/04/python-acc9c68ff62d73618344379ce3e645c9.png')     


def answer_check(msg):
    if msg.text == 'Да':
        bot.send_message(msg.chat.id, 'У тебя есть три попытки угадать число от 1 до 10')
        random_number = random.randint(1,10)
        p = 3
        start_game(msg, random_number, p)
        

    else:
        bot.send_message(msg.chat.id, 'Ну и ладно!')
    print(msg.text)

def start_game(msg, random_number, p):
    msg = bot.send_message(msg.chat.id, 'Введи число от 1 до 10: ')
    bot.register_next_step_handler(msg, check_func, random_number, p-1)


def check_func(msg, random_number, p):
    if msg.text == str(random_number):
        bot.send_message(msg.chat.id, 'Вы победили!')
    elif p == 0:
        bot.send_message(msg.chat.id, f'Вы проиграли! Число было - {random_number}')
    else:
        bot.send_message(msg.chat.id, f'Попробуй еще раз, у тебя осталось {p} попыток')
        start_game(msg, random_number, p)
# @bot.message_handler()
# def echo_all(message):
#     bot.send_message(message.chat.id, message.text)          #пересылает сообщения


    
bot.polling()






#git init
#git add .
#git commit -m 'names commit'
#git remote add origin ssh/https
#git push origin master