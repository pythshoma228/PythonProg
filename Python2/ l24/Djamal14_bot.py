import telebot

TOKEN = "NONE"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ['start'])
@bot.message_handler(commands = ['commands'])
@bot.message_handler(commands = ['info_bot'])

def answer(message):
	if message.text == "/start":
		bot.send_message(message.chat.id, "Привет! Ты начал разговор с ботом, напиши ему что-то!")

@bot.message_handler(func = lambda message: True)

def say_smth(message):
	if message.text == "commands":
		bot.send_message(message.chat.id, "/start, commands, info_bot")
	if message.text == "info_bot":
		bot.reply_to(message, "Бот не любит тупых вопросов так-как он сам тупой! Бот... ИНФОРМАЦИЯ ЗАШИФРОВАНА!!!")
	elif message.text == "Привет":
		bot.reply_to(message, "Дратути!")
	elif message.text == "Как дела?":
		bot.reply_to(message, "Отлично!!")
	elif message.text == "Что делаешь?":
		bot.reply_to(message, "С тобой разговариваю!")
	elif message.text == "Ты робот?":
		bot.reply_to(message, "Нет я многофункциональная машина!")
	elif message.text == "Привет":
		bot.reply_to(message, "Пока! Шутка!")
	elif message.text == "Ты тупой?":
		bot.reply_to(message, "Но уж поумнее тебя!!!!")
	else:
		bot.reply_to(message, "Я не понимаю что ты говоришь! Или в моей базе данных нет данного слова! ((((")

if __name__ == "__main__":
	bot.polling()
