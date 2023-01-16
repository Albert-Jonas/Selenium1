#Importálandók
import random

#Változók
min_password_length=1
max_password_length=30
length_of_password=0
password_chosen_characters_list=[]
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['%','^','&','@','#','$','-','_']
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','x','y','z','u','v','w']

#Függvények
#Igen/Nem kérdés függvény
#Bemenet: A kérdés szövege, string
#Kimenet: True(y), False (n)
def yes_no_question(QuestionString):
    response=''
    while (response!='Y') and (response!='N') and (response!='y') and (response!='n'):
        response=input(QuestionString)

    if response=='Y' or response=='y':
        return True
    else:
        return False

#Annak a megállapítása, hogy legyen-e szám a jelszóban?
have_a_number=yes_no_question('Do you want a number in your password (y/n):')
if have_a_number:
    min_password_length += 1

#Annak a megállapítása, hogy legyen-e szimbólum a jelszóban?
have_a_symbol=yes_no_question('Do you want a symbol in your password (y/n):')
if have_a_symbol:
    min_password_length += 1

#Annak a megállapítása, hogy legyen-e nagybetű a jelszóban?
have_capital_letter=yes_no_question('Do you want a capital letter in your password (y/n):')
if have_capital_letter:
    min_password_length += 1

#Kérjük be a jelszó hosszát.
while not((length_of_password>=min_password_length) and (length_of_password<=max_password_length)):
   length_of_password=int(input('Please give the number of characters of your password (' + str(min_password_length) +'-'+str(max_password_length)+') Type the number of characters!:'))

#Szedjük össze a megfeleleő számú és minősgúű karatereket.
#Ami biztosan kell a jelszóba
if have_a_number:
    password_chosen_characters_list.append(random.choice(numbers))

if have_a_symbol:
    password_chosen_characters_list.append(random.choice(symbols))

if have_capital_letter:
    password_chosen_characters_list.append(random.choice(letters).capitalize())

password_chosen_characters_list.append(random.choice(letters))

#A maradék karakterek kiválogatása
while len(password_chosen_characters_list)<length_of_password:
    what_type_of_characters=random.randint(0,3)
    if what_type_of_characters==0 and have_a_number:
        password_chosen_characters_list.append(random.choice(numbers))
    elif what_type_of_characters==1 and have_a_symbol:
        password_chosen_characters_list.append(random.choice(symbols))
    elif what_type_of_characters==2 and have_capital_letter:
        password_chosen_characters_list.append(random.choice(letters).capitalize())
    elif what_type_of_characters==3:
        password_chosen_characters_list.append(random.choice(letters))

#Keverés
random.shuffle(password_chosen_characters_list)

#Kiírás
print(*password_chosen_characters_list, sep='')