import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--lang= hu")

def startBrowser():
    driver = webdriver.Chrome()
    driver.get("https://www.desmos.com/scientific")
    return driver


def test(a,b,muvelet):
    for i in str(a):
        driver.find_element(By.CSS_SELECTOR, "span[aria-label='{}']".format(i)).click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "span[aria-label='{}']".format(muvelet)).click()
    time.sleep(2)
    for i in str(b):
        driver.find_element(By.CSS_SELECTOR, "span[aria-label='{}']".format(i)).click()

def eredmeny():

    vissza = driver.find_elements(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div[5]/div[2]/div[1]")
    # print(vissza.text)
    strErtak = ''
    for Item in vissza:
        strErtak += Item.text

    return strErtak[1:]

# driver.maximize_window()

# time.sleep(2)

# Ide kell az ellenőrző lépés

# test(1,2,"Összeadás")

# test(random.randint(0,9999999),random.randint(0,999999),"Kivonás")
# time.sleep(10)

def osszeadas_pozitiv_szamokkal(szam1, szam2):

    time.sleep(2)
    test(szam1, szam2,"Összeadás")
    time.sleep(2)
    eredmenystr = eredmeny()
    print(eredmenystr)

  # Bésző felállítása

    #meghajtjuk a böngészőt
    # test(2,3,"Plus")



    #ellenőrzés
    #segédfüggvény kell, ami kiszedi az eredményt a weboldalról és return-el visszaadja
    #segédfüggvény() == 5
    #összerakjuk a választ: kiíratjuk, hogy "osszeadas_pozitiv_szamokkal pass/fail fail esetben magyarázat

    #böngésző bezárása

driver = startBrowser()

# osszeadas_pozitiv_szamokkal(random.randint(1,9999999),random.randint(1,999999))
osszeadas_pozitiv_szamokkal(10,20)

# driver.close()