
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Remote("http://localhost:4444/wd/hub", DesiredCapabilities.CHROME)
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def toNumber(tag):
    return tag.text.replace(",", ".").replace("Bs = ", "")
    
def get_prices():

    driver.get("https://monitordolarvenezuela.com")
    parrafos = driver.find_elements(By.CLASS_NAME, "font-bold")
    time.sleep(0.5)
    prices = {
        "Dolar BCV" : toNumber(parrafos[3]),
        "Dolar Paralelo": toNumber(parrafos[5]),
        "Dolar Binance": toNumber(parrafos[7]),
        "Dolar Web": toNumber(parrafos[9]),
        "Dolar Today": toNumber(parrafos[11]),
        "Dolar Paralelo VIP": toNumber(parrafos[13])
    }   
    if prices["Dolar Paralelo"] == "0.00":
        print("err")
        get_prices()
    else:    
        return prices
print("si")
    #print(precio_BCV.text)
    #for i, parrafo in enumerate(parrafos):
    #    print(str(i) + " - " + parrafo.text)
