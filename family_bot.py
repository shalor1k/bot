import config
import telebot
from telebot import types
import numpy as np
import sqlite3
from sqlite3 import Error

data = [] #Данные для sql
confirm = False

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start', 'help'])

def answer_to_command(message):
	if message.text == '/start':
		bot.send_message(message.chat.id, 'Здравствуйте, я бот помогающий вам узнать причитаются ли вам меры социальной поддержки или льготы, если вы готовы начать напишите мне "Начинаем"')


@bot.message_handler(content_types=["text"])

def answer_to_text(message):
	if message.text.lower() == 'начинаем':
		msg = bot.send_message(message.chat.id, 'Первый вопрос: Являетесь ли вы гражданином РФ?')
		bot.register_next_step_handler(msg, secondAsk)

def secondAsk(message):
	if message.text.lower() == 'да' or message.text.lower() == 'нет':
		data.append(message.text)
		msg = bot.send_message(message.chat.id, 'Второй вопрос: Желаете ли вы оформить социальную льготу или услугу?')
		bot.register_next_step_handler(msg, thirdAsk)

	else:
		bot.send_message(message.chat.id,'Извините, я не понимаю ваш ответ')

def thirdAsk(message):
	if message.text.lower() == 'да' or message.text.lower() == 'нет':
		data.append(message.text)
		msg = bot.send_message(message.chat.id,'Упростить процесс получения до нескольких минут?')
		bot.register_next_step_handler(msg, fourthAsk)

	else:
		bot.send_message(message.chat.id,'Извините, я не понимаю ваш ответ')

def fourthAsk(message):
	if message.text.lower() == 'да':
		pass
		data.append(message.text)
	elif message.text.lower() == 'нет':
		data.append(message.text)
		keyboard = telebot.types.ReplyKeyboardMarkup(True)
		keyboard.row(u'\U00002705'+'Согласен', u'\U0000274C'+'Не согласен')
		msg = bot.send_message(message.chat.id, 'Ознакомьтесь с политикой обработки персональных данных перейдя по данной ссылке:', reply_markup=keyboard)
		bot.register_next_step_handler(msg, confirm_not_confirm)

def confirm_not_confirm(message):
	if 'Согласен' in message.text:
		data.append('Согласен')
		confirm = True
		msg = bot.send_message(message.chat.id, 'Вы подтвердили обработку ваших персональных данных.' + str(data))
	elif 'Не согласен' in message.text:
		data.append('Не согласен')
		confirm = False
		msg = bot.send_message(message.chat.id, 'Вы отказали обработку ваших персональных данных')


bot.polling(none_stop = True)
