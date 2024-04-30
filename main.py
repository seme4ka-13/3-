import requests
import telebot

TOKEN = '7075718203:AAHbuIi41waarvIXlI3BBrq6_iNOOIZ46K0'

bot = telebot.TeleBot(TOKEN)


def get_quote():
    try:
        # Запрос к API для получения цитаты
        response = requests.get("http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en")
        data = response.json()

        # Извлечение цитаты и автора
        quote = data['quoteText']
        author = data['quoteAuthor']

        return f'"{quote}"\n- {author}' if author else f'"{quote}"'
    except Exception as e:
        return "Извините, не могу получить цитату в данный момент."


# Обработчик команды /quote
@bot.message_handler(commands=['quote'])
def send_quote(message):
    quote = get_quote()
    bot.reply_to(message, quote)


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот, который отправляет случайные цитаты. Напиши /quote, чтобы получить цитату.")


# Обработчик неизвестных команд
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Извините, я не понимаю эту команду. Попробуйте /quote для получения цитаты.")


# Запуск бота
bot.polling()
