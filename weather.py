# import telebot
# import requests

# token ="5032530756:AAFcNkqLXeiXSl7uLnfz-HNIvzKK0ozB-OQ"
# # weather_api ="'https://api.openweathermap.org/data/2.5/weather?country={country}"
# weather_api = 'https://api.openweathermap.org/data/2.5/weather?q={country}'

# bot=telebot.TeleBot(token=token) 
# @bot.message_handler(command=['start'])
# def send(message):
#     bot.send_message(message.chat.id,'Привет напишите страну ')

# @bot.message_handler(content_types='text')
# def send_weather(message):
#     covid = requests.get(weather_api.format(country=message.text.title()))
#     weather_json = covid.json()
#     con = weather_json['main']['temp']
#     de = weather_json['main']['temp_max']
#     re = weather_json['main']['temp_min']
#     co = weather_json['main'][0]['main']
#     po = weather_json['main']['feels_like']
#     bot.send_message(message.chat.id, f'Температура { con }')
#     bot.send_message(message.chat.id, f'Максимальная температура { de }')
#     bot.send_message(message.chat.id, f'Минимальная температура { re }')
#     bot.send_message(message.chat.id, f'Ошущается как :{ co }')
#     bot.send_message(message.chat.id,f'Ошущается как : { po }')
#     # today = datetime.datetime.now()
#     # data = f'Количество заболевших коронавирусом в г. {message.text.title()}: {covid_json["All"]["confirmed"]} дата сегодня: {today.day}-{today.month}-{today.year}'
#     # bot.send_message(message.chat.id, data)
# print('Bot is ready')
# bot.infinity_polling()





import telebot
import requests
import json
import datetime


token='5032530756:AAFcNkqLXeiXSl7uLnfz-HNIvzKK0ozB-OQ'
bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(message.chat.id, "Привет, Я Погодагоп-бот напишите страну")

@bot.message_handler(content_types='text')
def send_data(message):
    API_key = 'ca47be775bcdce04caa140c563a84b6d'
    city = message.text.title()
    API = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_key}'
    data = requests.get(API).json()
    coord = data['main']['temp']
    flike = data['main']['feels_like']
    min_temp = data['main']['temp_min']
    max_temp = data['main']['temp_max']
    bot.send_message(message.chat.id, f"Температура:{coord} \n  Ощушается как:🤩{flike} /n Минимальная температура:🥶{min_temp} /n Максимальная температура:🥵{max_temp}")
        
        
print('Бот работает...')
bot.infinity_polling()