import random


def jelkeszlet(jelek):
    print(jelek)

def kisBetuk():
        return  ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


def nagyBetuk():
    kerdes = "a"
    while(kerdes not in "inIN"):
        kerdes = input("Nagybetűt tartalmazzon : (i/n)")
    if kerdes == "i" or "I":
        return ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T","U", "V", "W", "X", "Y", "Z"]
    else:return []

def szamok():
    kerdes = "a"
    while (kerdes not in "inIN"):
        kerdes = input("Számot tartalmazzon : (i/n)")
    if kerdes == "i" or "I":
        return  ["0","1","2","3","4","5","6","7","8","9"]
    else:return []

def kulunlegesJelek():
    kerdes = "a"
    while (kerdes not in "inIN"):
        kerdes = input("Különleges jelet tartalmazzon : (i/n)")
    if kerdes == "i" or "I":
        return ["^","&","@","#","$","-","_","!","$","%","~","?","=",">","<",".","*",";","+",":"]
    else:return []

def osszerak(jelek, hossz):
    vissza = ''
    for i in range (0,hossz):
        elemszam = random.randint(0,len(jelek)-1)
        vissza = vissza + jelek[elemszam]
    return vissza

def elemszam():
    vissza = 0
    while(int(vissza)< 5 or int(vissza)> 50):
        vissza = input('Kérek egy számot 5 - 50 között : (jelszó hossza) ')
    return int(vissza)


jelek = kisBetuk()
hossz = elemszam()
jelek = jelek +  nagyBetuk()
jelek = jelek + szamok()
jelek = jelek + kulunlegesJelek()
jelszo= osszerak(jelek, hossz)
# jelkeszlet(jelek)
print('Generált Jelszó : ' + jelszo)