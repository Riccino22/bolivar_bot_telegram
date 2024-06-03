import telebot
import scraper
import os
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.environ.get("TELEGRAM_TOKEN"))

@bot.message_handler(commands=["start"])
def start_command(m):   
    print("Sended")
    prices = scraper.get_prices()
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
    dt = table.data.drop(columns=['fecha'])
    to_text = dt.to_string()
    bot.reply_to(m, to_text)

@bot.message_handler(commands=["bcv"])
def bcv_command(m):
    bot.reply_to("SI")

bot.polling(timeout=120)  # Aumenta el tiempo de espera a 60 segundos
""