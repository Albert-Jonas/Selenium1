import random


def listaKiiro(szoveg,lista):
    print(szoveg)
    print(lista)
    print("/***/")

def elemvalasztoSor():
    vissza = [0,0,0,0,0]
    for i in range(0,5):
        if i < 4:
            vissza[i] = random.randint(0, 1)
        else:
            vissza[i] = random.randint(5, 55)
    return vissza

def osszerak(hossz, jelkeszlet):
    vissza = ""
    for i in range(0, hossz):
        rndSzam = random.randint(0, len(jelkeszlet))
        # print(jelkeszlet[rndSzam])
        vissza += jelkeszlet[rndSzam]
    return vissza


def jelkeszletOsszerako(elemValasztoSor):
    nagybetu = []
    kisbetu = []
    szam = []
    kulonlegesJelek = []
    for i in range(0, 4):
        if i == 0 and elemValasztoSor[i] == 1:
           nagybetu = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T","U", "V", "W", "X", "Y", "Z"]
        if i == 1 and elemValasztoSor[i] == 1:
            kisbetu = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
             "v", "w", "x", "y", "z"]
        if i == 2 and elemValasztoSor[i] == 1:
            szam = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        if i == 3 and elemValasztoSor[i] == 1:
            kulonlegesJelek = ["^","&","@","#","$","-","_","!","$","%","~","?","=",">","<",".","*",";","+",":"]
    return nagybetu + kisbetu + szam + kulonlegesJelek

def kever(jelkeszlet):

    for i in range(0,len(jelkeszlet)):
        temp = jelkeszlet[i]

        elemszam= random.randint(0, len(jelkeszlet)-1)
        masodikElem = jelkeszlet[elemszam]

        jelkeszlet[elemszam] = temp
        jelkeszlet[i] = masodikElem

    return jelkeszlet




elemValasztoSor = elemvalasztoSor()
listaKiiro("Választó sor:",elemValasztoSor)
# Sort ellenőrizni, hogy ne legyen mindegyik 0

jelkeszlet = jelkeszletOsszerako(elemValasztoSor)
listaKiiro("Jelkészlet ", jelkeszlet)

jelkeszlet = kever(jelkeszlet)
listaKiiro("Jelkészlet Kevert", jelkeszlet)

jelszo = osszerak(elemValasztoSor[4], jelkeszlet)
print(jelszo)