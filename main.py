#Selenium Tutorial #1
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.implicitly_wait(2.0)


wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=[])


driver.get("https://google.com")

time.sleep(0.5)

#Accept the agreement
driver.execute_script('return document.querySelector("#L2AGLb > div")').click()

box = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")))
box.send_keys("Python")

button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]")))
button.click()

#box.send_keys(Keys.RETURN)

time.sleep(5)
driver.close()

