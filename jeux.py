import random

borne1 = input("Saisissez un nombre qui sera la plus petite borne :")
while True :
    try :
        borne1 = int(borne1)
        break
    except :
        borne1 = input("Saisissez un nombre qui sera la plus petite borne :")

borne2 = input("Saisissez un nombre qui sera la plus grande borne :")
while True :
    try :
        borne2 = int(borne2)
        if borne1 >= borne2 :
            print("Saisissez un nombre plus grand que : ", borne1)
            borne2 = input()
        else :
            break
    except :
        borne2 = input("Saisissez un nombre qui sera la plus grande borne :")

nombre = random.randint(borne1, borne2)
while True:
    print("Saisissez un nombre entre ", borne1, " et ", borne2, " :")
    saisi = input()
    try :
        saisi = int(saisi)
    except:
        saisi = input("Saisissez un nombre :")
    if saisi == nombre :
        print("c'est gagné")
        break
    elif saisi > nombre :
        print("trop grand")
        if borne2 >= saisi :
            borne2 = saisi - 1
    else :
        print("trop petit")
        if borne1 <= saisi :
            borne1 = saisi + 1
