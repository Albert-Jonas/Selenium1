def kisBetuk():
    return ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    # for i in lista:
    #     print(i)
def nagyBetuk():
   return ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def szamok():
     return ["0","1","2","3","4","5","6","7","8","9"]
def kulunlegesJelek():
   return ["^","&","@","#","$","-","_","!","$","%","~","?","=",">","<",".","*",";","+",":"]

def elemszam():
    pass


jelek = kisBetuk()
jelek = jelek +  nagyBetuk()
jelek = jelek + szamok()
jelek = jelek + kulunlegesJelek()



hossz = elemszam()

for i in jelek:
    print(i)