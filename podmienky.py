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