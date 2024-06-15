import scraper
import csv
from datetime import datetime
import pandas as pd

def update(prices_scraped):
    with open("prices.csv", "r") as file:
        reader = csv.DictReader(file)
        prices = list(reader)

    actual_state = prices_scraped
    prices.append(actual_state)

    with open("prices.csv", "w") as file:
        fields = prices[0].keys()
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(prices)

def info(date):
    with open("prices.csv", "r") as file:
        reader = csv.DictReader(file)
        prices = list(reader)
    prices_info = ""
    
    for price in prices:
        if price["Datetime"].startswith(date):
            prices_info += f"""
*{price["Datetime"].replace(" ", "\n")}*
            
    Dolar BCV: {price["Dolar BCV"]}
    Dolar Paralelo: {price["Dolar Paralelo"]}
    Dolar Binance: {price["Dolar Binance"]}
    Dolar Web:  {price["Dolar Web"]}
    Dolar Today: {price["Dolar Today"]}
    Dolar Paralelo VIP: {price["Dolar Paralelo VIP"]}
            """
    return prices_info
    
