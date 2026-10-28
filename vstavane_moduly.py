import math
def vypocet_objemu_kuzela(polomer, vyska):
    objem = (1.0/3.0) * math.pi * math.pow(polomer,2) * vyska
    return objem

def povrch_kuzela(polomer,vyska):
    polomer_plasta = math.sqrt(math.pow(vyska,2) + math.pow(polomer,2))
    povrch = math.pi * polomer* polomer_plasta
    return povrch

polomer = float(input("Zadaj polomer kužeľa"))
vyska = float(input("Zadaj výšku kužeľa"))

print(f"Objem kužeľa je : {vypocet_objemu_kuzela(polomer,vyska)}")
print(f"Obsah kužeľa je : {povrch_kuzela(polomer,vyska)}")

import random
#Vygenerujeme náhodné číslo medzi 1 .. 10
print(f"Náhodné číslo 1 až 10: {random.randint(1,10)}")

zoznam = [1,2,3,4,5,6]
print(zoznam)

random.shuffle(zoznam)
print(f"Premiešaný zoznam : {zoznam}")
