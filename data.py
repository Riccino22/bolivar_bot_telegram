import scraper
import csv
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

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
    
def graph(exchange):
    match exchange:
        case "bcv":
            exchange_name = "Dolar BCV"
        case "par":
            exchange_name = "Dolar Paralelo"
        case "bin":
            exchange_name = "Dolar Binance"
        case "parvip":
            exchange_name = "Dolar Paralelo VIP"
        case _:
            exchange_name = "Dolar BCV"
            
    df = pd.read_csv("prices.csv", parse_dates=["Datetime"])
    # Crear un gráfico
    ax = df.plot(x="Datetime", y=exchange_name, figsize=(10, 10))
    ax.set_title('Evolución del ' + exchange_name)
    ax.set_xlabel('Fecha')
    ax.set_ylabel('Precio en Bolívares')
    plt.grid(True)
    plt.savefig("dolar_bcv_plot.png")  # Guardar el gráfico como una imagen
    plt.close()  # Cerrar el gráfico para liberar memoria

    return "dolar_bcv_plot.png"