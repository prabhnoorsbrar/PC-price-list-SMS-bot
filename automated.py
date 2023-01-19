from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
#PATH TO CHROME WEBDRIVER
#location varies user to user, wherever you extract the webdriver would be where the path is
PATH = "C:\Program Files (x86)\chromedriver.exe"
#function that scrapes a pc builder website to gather total price for PC parts list
def scrape_pc_picker():
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(10)
    #this link can be to a price list that you have
    driver.get("https://pcpartpicker.com/list/wzhByK")
    driver.maximize_window()

    all_prices = driver.find_elements(By.CLASS_NAME,"td__price")
    price_of_parts = []
    
    #add price to list of price parts
    for p in all_prices:
        price_of_parts.append(p.text)
    
    return price_of_parts
