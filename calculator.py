import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--lang= hu")

def test(a,b,muvelet):
    for i in str(a):
        driver.find_element(By.CSS_SELECTOR, "span[aria-label='{}']".format(i)).click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "span[aria-label='{}']".format(muvelet)).click()
    time.sleep(2)
    for i in str(b):
        driver.find_element(By.CSS_SELECTOR, "span[aria-label='{}']".format(i)).click()

driver = webdriver.Chrome()
# driver.maximize_window()

driver.get("https://www.desmos.com/scientific")

time.sleep(2)

# Ide kell az ellenőrző lépés

# test(1,2,"Összeadás")

test(random.randint(0,9999999),random.randint(0,999999),"Minus")
# time.sleep(10)


def osszeadas_pozitiv_szamokkal():

    #böngésző felállítása

    #meghajtjuk a böngészőt
    test(2,3,"Plus")

    #ellenőrzés
    #segédfüggvény kell, ami kiszedi az eredményt a weboldalról és return-el visszaadja
    #segédfüggvény() == 5
    #összerakjuk a választ: kiíratjuk, hogy "osszeadas_pozitiv_szamokkal pass/fail fail esetben magyarázat

    #böngésző bezárása