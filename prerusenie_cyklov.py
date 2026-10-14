for i in range(10):
    if i == 5:
        break #prerušenie for cyklu
    print(i)

print("Výpis nepárnych čísiel:")
#prerušenie otočky cyklu
for i in range(10):
    if i % 2 == 0: #prerusenie parne cisla
        continue
    print(i)

print("Výpis párnych čísiel:")
#prerušenie otočky cyklu
for i in range(10):
    if i % 2 != 0: #prerusenie parne cisla
        continue
    print(i)

#vnorené cykly
for i in range(1,6):
    for j in range(i):
        print("*", end="") #end="" -- zruší odriadkovanie
    print("")

