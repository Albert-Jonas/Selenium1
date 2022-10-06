#Selenium Tutorial #1

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.implicitly_wait(2.0)

driver.get("https://google.com")

time.sleep(0.5)

#Accept the agreement
time.sleep(2)
driver.execute_script('return document.querySelector("#L2AGLb > div")').click()

box = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
box.send_keys("Python")
time.sleep(2)
box.send_keys(Keys.RETURN)

time.sleep(5)
driver.close()

