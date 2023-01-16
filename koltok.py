from builtins import range, list

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

link = "https://hu.wikipedia.org/wiki/Magyar_k%C3%B6lt%C5%91k,_%C3%ADr%C3%B3k_list%C3%A1ja"

lista = []

driver = webdriver.Chrome()
driver.get(link)

lista = driver.find_elements(By.PARTIAL_LINK_TEXT, " ")

for i in range(0, len(lista)):

    credIdValue = lista[i].find_elements(By.XPATH("./text"))
    lista[i] = lista[i].text + " " + credIdValue.text
    print(lista[i].text.split(" "))

driver.close()