import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import Workbook, load_workbook

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--lang= hu")

wb = load_workbook('excel.xlsx')
ws = wb["Összeadás"]

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
    strErtek = ""
    for Item in vissza:
        strErtek += Item.text
    return strErtek[1:]

# driver.maximize_window()
# test(random.randint(0,9999999),random.randint(0,999999),"Kivonás")
# time.sleep(10)





    #ellenőrzés
    #segédfüggvény kell, ami kiszedi az eredményt a weboldalról és return-el visszaadja
    #segédfüggvény() == 5
    #összerakjuk a választ: kiíratjuk, hogy "osszeadas_pozitiv_szamokkal pass/fail fail esetben magyarázat

    #böngésző bezárása



# osszeadas_pozitiv_szamokkal(random.randint(1,9999999),random.randint(1,999999))
# osszeadas_pozitiv_szamokkal(10,20)
# assert "30" == osszeadas_pozitiv_szamokkal(10,20,30)
def biralat(szam3, eredmenystr):
    try:
        assert str(szam3)  == eredmenystr, "Hibás"
    except AssertionError as e:
        ws['F' + str(i)] = "Fail"
        ws['G' + str(i)] = str(e)
    else:
        ws['F' + str(i)] = "Pass"


def osszeadas_pozitiv_szamokkal(szam1, szam2, szam3, i):
    time.sleep(2)
    test(szam1, szam2, "Összeadás")
    time.sleep(2)
    eredmenystr = eredmeny()
    biralat(szam3, eredmenystr)
    # try:
    #     assert str(szam3) == eredmenystr, "Hibás"
    # except AssertionError as e:
    #     ws['F' + str(i)] = "Fail"
    #     ws['G' + str(i)] = str(e)
    # else:
    #     ws['F' + str(i)] = "Pass"



def kivonas_pozitiv_szamokkal(szam1, szam2, szam3):
    time.sleep(2)
    test(szam1, szam2, "Kivonás")
    time.sleep(2)
    eredmenystr = eredmeny()
    assert szam3 == eredmenystr, "Hibás"
def szorzas_pozitiv_szamokkal(szam1, szam2, szam3):
    time.sleep(2)
    test(szam1, szam2, "Szorzás")
    time.sleep(2)
    eredmenystr = eredmeny()
    assert szam3 == eredmenystr, "Hibás"
def osztas_pozitiv_szamokkal(szam1, szam2, szam3):
    time.sleep(2)
    test(szam1, szam2, "Osztás")
    time.sleep(2)
    eredmenystr = eredmeny()
    assert szam3 == eredmenystr, "Hibás"


def clear():
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div[3]/div[1]/div/div[7]").click()




driver = startBrowser()
#osszeadas_pozitiv_szamokkal(10,20,"30")
#clear()
#kivonas_pozitiv_szamokkal(20,10,"10")
#clear()
#szorzas_pozitiv_szamokkal(10,20,"200")
#clear()
#osztas_pozitiv_szamokkal(10,20,"0.5")
#clear()

def excelReset():
    i=3
    while (ws['B' + str(i)].value):
        ws['F' + str(i)] = " "
        ws['G' + str(i)] = str(" ")
        i = i + 1


excelReset()
i = 3
while(ws['B'+str(i)].value):
    osszeadas_pozitiv_szamokkal(ws['B'+str(i)].value, ws['C'+str(i)].value, ws['D'+str(i)].value, i)
    i = i + 1
    clear()

wb.save('excel.xlsx')
driver.close()
# driver.close()