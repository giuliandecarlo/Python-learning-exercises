import random
import string
import os


def passwordGenerator():
    pwLength=0
    specialCh=None
    numbers=None
    upCase=None
    while((pwLength<5)or(pwLength>16)):                    #Viene richiesta la lunghezza della password da generare
        try:
            pwLength=int(input("Enter the length of the password:  [min:5|max:16]"))
        except:
            pwLength=1

    while((specialCh!=True)and(specialCh!=False)):        #Viene chiesto se inserire caratteri speciali
        spch=input("Include Symbols:  [Y|N]")
        if((spch=="Y") or (spch=="y")):
            specialCh=True
        elif((spch=="N") or (spch=="n")):
            specialCh=False
    
    while((numbers!=True)and(numbers!=False)):            #Viene chiesto se inserire numeri
        nb=input("Include Numbers:  [Y|N]")
        if((nb=="Y") or (nb=="y")):
            numbers=True
        elif((nb=="N") or (nb=="n")):
            numbers=False
    
    while((upCase!=True)and(upCase!=False)):              #Viene chiesto se inserire caratteri in maiuscolo
        uc=input("Include Uppercase Characters:  [Y|N]")
        if((uc=="Y") or (uc=="y")):
            upCase=True
        elif((uc=="N") or (uc=="n")):
            upCase=False

#Vengono combinati i vari i casi in base alle scelte effettuate
    lower = string.ascii_lowercase
    total=lower
    if(specialCh==True):
        symb = string.punctuation
        total=total+symb
    if(numbers==True):
        num = string.digits
        total=total+num
    if(upCase==True):
        upper = string.ascii_uppercase
        total=total+upper

#La password viene generata casualmente
    temp = random.sample(total,pwLength)
    pw = "".join(temp)                   
    return(pw)


def pwManager():                               #vengono richieste altre informazioni utili 
    print("Welcome to the Password Manager:")
    while(True):
        checkNext=False
        saveInFile=None
        name=input("Insert the name of the element: ")
        username=input("Insert the username: ")
        password=passwordGenerator()
        print("Your password has been successfully generated!")
    #
        while((saveInFile!=True)and(saveInFile!=False)):
            save=input("Do you want to save this information in a txt file?  [Y|N]")
            if((save=="Y") or (save=="y")):
                saveInFile=True
            elif((save=="N") or (save=="n")):
                saveInFile=False
        if(saveInFile==True):
            with open("password1.txt", "a") as f:
                information="|Name: "+name+" |Username: "+username+" |Password: "+password+"\n"
                f.writelines(information)

        while(checkNext==False):
            nextEl=input("Do you want to insert a new element?  [Y|N]")
            if((nextEl=="N")or(nextEl=="n")):
                checkNext=True
                exit()
            elif((nextEl=="Y")or(nextEl=="y")):
                checkNext=True
                os.system('cls' if os.name == 'nt' else 'clear')
pwManager()