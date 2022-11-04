from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.desmos.com/scientific")
driver.maximize_window()


driver.find_element(By.xpath, value="lastName").send_keys("bo2023")
