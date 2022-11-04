from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()

driver.get("https://www.desmos.com/scientific")
driver.maximize_window()

time.sleep(2)


def test(a,b,muvelet):
    driver.find_element(By.CSS_SELECTOR, "span[aria-label='{}']".format(a)).click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "span[aria-label='{}']".format(muvelet)).click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "span[aria-label='{}']".format(b)).click()

    #Ide kell az ellenőrző lépés

test(1,2,"Plus")
