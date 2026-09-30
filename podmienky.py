cislo = int(input("Zadaj celé číslo: "))

if cislo > 0:
    print("Zadal si kladné číslo !")
else:
    if cislo == 0:
        print("Zadal si nulu !")
    else:
        print("Zadal si záporné číslo! ")

if cislo > 0:
    print("Zadal si kladné číslo !")
elif cislo == 0:
        print("Zadal si nulu !")
else:
        print("Zadal si záporné číslo! ")

#Niekedy potrebujeme zistiť, či číslo je z intervalu
if cislo >= 0 and cislo <= 100:
    print("Číslo je z intervalu 0 .. 100 !")
else:
    print("Číslo nie je z intervalu 0 .. 100 !")

text = 'Toto je text, ktorý obsahuje slovo Python'
if "Python" in text:
    print("Text obsahuje slovo Python !")

#mnohonásobné vetvenie
hodnota = 10
match hodnota:
    case 1:
        print("Zadal si jedna !")
    case 2:
        print("Zadal si dva !")
    case 3:
        print("Zadal si tri !")
    case 4:
        print("Zadal si štyri !")
    case 5:
        print("Zadal si päť !")
    case _:
        print("Zadal si niečo iné ! ")