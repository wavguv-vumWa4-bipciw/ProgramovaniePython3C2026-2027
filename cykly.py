#nekonečný cyklus while
pocitadlo = 0
while pocitadlo <= 5:
    print(f"Hodnota pocitadla je : {pocitadlo}")
    pocitadlo +=1

#cyklus s konečným počtom opakovaní for
vysledok = 1
cislo_faktorial = int(input("Zadaj číslo na výpočet faktoriálu : "))
for cislo in range(1,cislo_faktorial+1):
    vysledok *= cislo
print(f"Výsledok faktoriálu je {vysledok}")

beziaci_program = True
while beziaci_program:
    print("1 - Výpočet faktoriálu")
    print("2 - Výpočet priemeru")
    print("3 - Výpočet obsahu kocky")
    print("4 - Výpočet obsahu obdĺžnika")
    print("5 - koniec programu")
    volba = int(input('Vyber si : '))
    match volba:
          case 5:
              beziaci_program = False
          case _:
              print("Vyber voľbu od 1 .. 5")
    input("Pre pokracovanie stlač Enter !")

