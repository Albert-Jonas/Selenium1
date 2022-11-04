import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#megnyitjuk a weboldalt
driver.get("https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp")
driver.maximize_window()

#megkeressük a funkciót amit tesztelünk

#driver.find_element(By.LINK_TEXT, value="Fiók létrehozása").click()
time.sleep(3)

#bevisszük az adatokat ami a bemeneti mezőkhöz kell
driver.find_element(By.NAME, value="lastName").send_keys("bo2023")
driver.find_element(By.NAME, value="firstName").send_keys("no")
time.sleep(2)
driver.find_element(By.NAME, value="Username").send_keys("bo2023no")
driver.find_element(By.NAME, value="Passwd").send_keys("Vanek2022")
time.sleep(3)
driver.find_element(By.NAME, value="ConfirmPasswd").send_keys("Vanek2022")
time.sleep(3)
driver.find_element(By.CLASS_NAME, value="VfPpkd-muHVFf-bMcfAe").click()
time.sleep(2)
driver.find_element(By.ID, value="accountDetailsNext").click()

#ellenőrizzük, hogy oda jutottunk e, ahova szeretnénk

time.sleep(2)
if "Telefonszám igazolása" == driver.find_element(By.ID, "headingText").text:
    print("pass")
else:
    print("fail")
