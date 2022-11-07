import sys

from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()

driver.get("https://www.desmos.com/scientific")
# driver.maximize_window()

time.sleep(2)

def test(a,b,muvelet):
    for i in str(a):
        driver.find_element(By.CSS_SELECTOR, "span[aria-label='{}']".format(i)).click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "span[aria-label='{}']".format(muvelet)).click()
    time.sleep(2)
    for i in str(b):
        driver.find_element(By.CSS_SELECTOR, "span[aria-label='{}']".format(i)).click()

    #Ide kell az ellenőrző lépés

# test(1,2,"Összeadás")
test(57123,945576,"Kivonás")
