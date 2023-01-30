from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


@pytest.fixture
def webdriver_stuff():
    global driver
    driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    yield

    time.sleep(3)
    driver.close()


def test_shopping_main(webdriver_stuff):
    driver.find_element(By.CLASS_NAME, "inventory_item_name").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    listazott_elemek = driver.find_elements(By.CLASS_NAME, "inventory_item_name")

    if any(item.text == "Sauce Labs Backpack" for item in listazott_elemek):
        pass
    else:
        pytest.fail("Nince benne a kosárban a termék")

    driver.find_element(By.ID, "checkout").click()

    if not (driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"):
        pytest.fail("Nem értünk el a végállapotba")


def test_shopping_3a(webdriver_stuff):
    driver.find_element(By.CLASS_NAME, "inventory_item_name").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    driver.find_element(By.ID, "continue-shopping").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    listazott_elemek = driver.find_elements(By.CLASS_NAME, "inventory_item_name")

    if any(item.text == "Sauce Labs Backpack" for item in listazott_elemek):
        if any(item.text == "Sauce Labs Bolt T-Shirt" for item in listazott_elemek):
            pass
        else:
            pytest.fail("Nincs bennea T-shirt")
    else:
        pytest.fail("Nincs benne a Backpack")

    driver.find_element(By.ID, "checkout").click()

    assert (driver.current_url, "https://www.saucedemo.com/checkout-step-one.html",
            "Nem értünk el a végállapotba")