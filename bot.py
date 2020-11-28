import telebot
import config
from telebot import types
import random
import qrcode
from PIL import Image
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	c1 = types.KeyboardButton("Оформить заказ")
	markup.add(c1)
	bot.send_message(
		message.chat.id, 'Привет! Добро пожаловать в кофейню!', reply_markup=markup
	)

@bot.message_handler(content_types=['text'])
def usualMessage(message):
	if message.text == "Оформить заказ" :
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
		c1 = types.KeyboardButton("Американо")
		c2 = types.KeyboardButton("Каппучино")
		c3 = types.KeyboardButton("Мокко")
		c4 = types.KeyboardButton("Эспрессо")
		c5 = types.KeyboardButton("Латте")
		markup.add(c1,c2,c3,c4,c5)
		bot.send_message(
			message.chat.id, 'Выбери напиток!', reply_markup=markup
		)
	if message.text == "Американо" or message.text == "Каппучино" or message.text == "Мокко" or message.text == "Эспрессо" or message.text == "Латте":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
		c1 = types.KeyboardButton("Да")
		c2 = types.KeyboardButton("Нет, вернуться к предыдущему шагу")
		markup.add(c1, c2)
		bot.send_message(
			message.chat.id, f'Твой заказ : {message.text}', reply_markup=markup
		)
	if message.text == "Да":
		codeToGet = random.randint(100000, 999999)
		img = qrcode.make('wefwee').save(f'img/qr{codeToGet}.png')
		bot.send_message(
			message.chat.id, 'Когда будешь в кофейне, покажи это сообщение оператору!'
		)
		img = Image.open(f'img/qr{codeToGet}.png')
		bot.send_photo(message.chat.id, img)
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
		c1 = types.KeyboardButton("Оформить заказ")
		markup.add(c1)
		bot.send_message(message.chat.id, 'Перейди к новому заказу!', reply_markup = markup)
bot.polling(none_stop=True)