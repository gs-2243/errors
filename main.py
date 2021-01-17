from config import TOKEN
import telebot
import requests
import json

keys = {
    "доллар" "USD"
    "Рубль" "RUB"
    "Евро" "EURO"
}

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=["start", "help"])
def echo(message: telebot.types.Message):
    text = "Чтобы начать работу введите команду боту команду в следующем фомате:<имя валюты>\n <в какую вадты " \
           "перевести> \n" \
           "《Колличество переводимой валюты》"

    bot.reply_to(message, text)
@bot.message_handler(commands=["values"])
def values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for key in keys.keys():
        text = "\n".join((text, key))
        bot.reply_to(message, text)



bot.polling()
