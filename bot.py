import telebot
import scraper
import os
from dotenv import load_dotenv
import data
load_dotenv()

bot = telebot.TeleBot(os.environ.get("TELEGRAM_TOKEN"))

@bot.message_handler(commands=["start"])
def start_command(m):   
    print("Sended")
    prices = scraper.get_prices()
    prices["Dolar BCV"]
    data.update(prices)
    bot.reply_to(m, f"""
        Bienvendido a Bolivares Bot
        Dolar BCV: {prices["Dolar BCV"]}
        Dolar Paralelo: {prices["Dolar Paralelo"]}
        Dolar Binance: {prices["Dolar Binance"]}
        Dolar Web:  {prices["Dolar Web"]}
        Dolar Today: {prices["Dolar Today"]}
        Dolar Paralelo VIP: {prices["Dolar Paralelo VIP"]}
    """)

@bot.message_handler(commands="info")
def info_command(m):
    try:    
        bot.reply_to(m, data.info(m.text.replace("/info ", "")), parse_mode='Markdown')
    except telebot.apihelper.ApiTelegramException:
        bot.reply_to(m, "Para ver la informacion de una fecha especifica: /info AAAA-MM-DD")


@bot.message_handler(commands="history")
def history_command(m):
    with open(data.graph(m.text.replace("/history ", "")), 'rb') as image:
        bot.send_photo(m.chat.id, image)
        

@bot.message_handler(commands=["bcv"])
def bcv_command(m):
    bot.reply_to("SI")

bot.polling(timeout=120)  # Aumenta el tiempo de espera a 60 segundos
""