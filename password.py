from random import random, randint

def kisBetuk():
    return ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def nagyBetuk():
    kerdes = input("Nagybetűt tartalmazzon: (i/n) ")
    if kerdes == "i":
        return ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    else:
        return []
def szamok():
    kerdes = input("Számokat tartalmazzon: (i/n) ")
    if kerdes == "i":
        return ["0","1","2","3","4","5","6","7","8","9"]
    else:
        return []
def kulunlegesJelek():
    kerdes = input("Különleges jeleket tartalmazzon: (i/n) ")
    if kerdes == "i":
        return ["^","&","@","#","$","-","_","!","$","%","~","?","=",">","<",".","*",";","+",":"]
    else:
        return []
def elemszam():
    return input("Kérek egy számot 5-50 közőtt: (Jelszó hossza) ")

def osszerak(jelek, hossz):
    vissza = ""
    for i in range(0,hossz):
        elemSzam = randint(0,len(jelek))
        db = jelek[elemSzam]
        # print(db)
        vissza = vissza + db
    return vissza


jelek = kisBetuk()
hossz = elemszam()
jelek = jelek +  nagyBetuk()
jelek = jelek + szamok()
jelek = jelek + kulunlegesJelek()
jelszo= osszerak(jelek, int(hossz))
print(jelszo)