from bs4 import BeautifulSoup
import telebot
import scraping
import table
import os


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start_command(m):   
    scraping.start_scraping()
    bot.reply_to(m, f"""
        Bienvendido a Bolivares Bot
        Dolar BCV: {scraping.precios["Dolar BCV"]}
        Dolar Paralelo: {scraping.precios["Dolar Paralelo"]}
        Dolar Binance: {scraping.precios["Dolar Binance"]}
        Dolar Web:  {scraping.precios["Dolar Web"]}
        Dolar Today: {scraping.precios["Dolar Today"]}
        Dolar Paralelo VIP: {scraping.precios["Dolar Paralelo VIP"]}
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
