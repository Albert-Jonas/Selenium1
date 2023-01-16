from builtins import range, list, str
from openpyxl.reader.excel import load_workbook
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "https://hu.wikipedia.org/wiki/Magyar_k%C3%B6lt%C5%91k,_%C3%ADr%C3%B3k_list%C3%A1ja"

lista = []
wb = load_workbook("koltok.xlsx")
ws = wb["költök"]
excelFejlec= ["Köktő neve", "Születési helye", "Születés időpontja", "Halála ideje"]

# ---------------------------------Excel műveletel
#Excel tábla kiüritése
def excelUrites():
    i = 1
    while (ws['A' + str(i)].value):
        ws['A' + str(i)] = " "
        i = i + 1
# Excel tábla mentése
def excelMentes():
    wb.save("koltok.xlsx")

# Excel fejlécek beírása a táblázatba
def excelFejlecBeallitas():
    ws["A" + "1"] = excelFejlec[0]
    ws["B" + "1"] = excelFejlec[1]
    ws["C" + "1"] = excelFejlec[2]
    ws["D" + "1"] = excelFejlec[3]

def excelListaMentes(lista):

    # for i in range(0, len(lista)):
    for i in range(0, 100):
        print(lista[i].text)
        ws["A" + str(i+2)] = lista[i].text


# -------------------------------------Web műveletek
def openBrowser():
    driver = webdriver.Chrome()
    driver.get(link)
    driver.minimize_window()
    return driver




# Lista létrehozása a wiki oldalról
# def openBrowswer():


def koltoLista(driver):
    lista = driver.find_elements(By.PARTIAL_LINK_TEXT, " ")
    return lista

def weblapBezarasa():
    driver.quit()



excelUrites()
excelFejlecBeallitas()
excelMentes()



driver = openBrowser()
lista = koltoLista(driver)
# excelListaMentes(driver)

