from random import random, randint

import logging

logging.basicConfig(filename='Password.log', filemode='w', encoding='utf-8', level=logging.INFO)
def jelkeszlet(jelek):
    print(jelek)
def kerdesFG(szoveg):
    return input(szoveg)

def kisBetuk():
    return ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# def nagyBetuk():
#     kerdes = kerdesFG("Nagybetűt tartalmazzon: (i/n) ")
#     if kerdes == "i":
#         return ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#     else:
#         return []

def nagyBetuk2():
    # jelkeszlet(jelek)
    kerdes = "a"
    while(kerdes not in "inIN"):
        kerdes = kerdesFG("Nagybetűt tartalmazzon: (i/n) ")
    if kerdes == "i":
        return ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                "U", "V", "W", "X", "Y", "Z"]
    else: return []

# def szamok():
#     kerdes = kerdesFG("Számokat tartalmazzon: (i/n) ")
#     if kerdes == "i":
#         return ["0","1","2","3","4","5","6","7","8","9"]
#     else:
#         return []

def szamok2():
    kerdes = "a"
    # jelkeszlet(jelek)
    while (kerdes not in "inIN"):
        kerdes = kerdesFG("Számokat tartalmazzon: (i/n) ")
        # print(kerdes)

    if kerdes == "i":
        return ["0","1","2","3","4","5","6","7","8","9"]
    else:
        return []
# def kulunlegesJelek():
#     kerdes = kerdesFG("Különleges jeleket tartalmazzon: (i/n) ")
#     if kerdes == "i":
#         return ["^","&","@","#","$","-","_","!","$","%","~","?","=",">","<",".","*",";","+",":"]
#     else:
#         return []
def kulunlegesJelek2():
    kerdes = "a"
    # jelkeszlet(jelek)
    while (kerdes not in "inIN"):
        kerdes = kerdesFG("Különleges jeleket tartalmazzon: (i/n) ")
    if kerdes == "i":
        return ["^","&","@","#","$","-","_","!","$","%","~","?","=",">","<",".","*",";","+",":"]
    else:
        return []
def elemszam():
    return input("Kérek egy számot 5-50 közőtt: (Jelszó hossza) ")
def osszerak(jelek, hossz):
    vissza = ""
    # jelkeszlet(jelek)
    for i in range(0,int(hossz)):
        elemSzam = randint(0,len(jelek)-1)
        db = jelek[elemSzam]
        # print(db)
        vissza = vissza + db
        # print(str(i) + " - " + vissza )

    return vissza

def elemszam2():
    vissza = 0
    while (int(vissza) < 5 or int(vissza) > 50):
        vissza = input("Kérek egy számot 5-50 közőtt: (Jelszó hossza) ")
        # print(vissza)
    return vissza

logging.info("Start")
jelek = kisBetuk()
logging.info("kisbetük után a jelkészlet :" + jelek)
hossz = elemszam2()
logging.info("Password hossza : "+hossz)
jelek = jelek +  nagyBetuk2()
jelek = jelek + szamok2()
jelek = jelek + kulunlegesJelek2()
jelszo= osszerak(jelek, hossz)
print(jelszo)

