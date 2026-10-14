def objem_kvadra(a,b,c):
    objem = a*b*c
    return objem

def obsah_kvadra(a,b,c):
    obsah = 2*(a*b+a*c+b*c )
    return obsah

strana_a = float(input("Zadaj stranu A valca : "))
strana_b = float(input("Zadaj stranu B valca : "))
strana_c = float(input("Zadaj stranu C valca : "))

print(f"Objem kvádra je : {objem_kvadra(strana_a,strana_b,strana_c)}")
print(f"Obsah kvádra je : {obsah_kvadra(strana_a,strana_b,strana_c)}")

#vlastná funkcia na výpočet hodnoty PI
def vypocitaj_pi(pocet_iteracii):
    pi = 0
    znamienko = 1

    for i in range(pocet_iteracii):
        pi += znamienko / (2 * i + 1)
        znamienko *= -1

    return 4 * pi

def objem_kuzela(polomer = 1.0, vyska=1.0):
    objem = (1.0/3.0)*vypocitaj_pi(1000) * polomer * polomer * vyska
    return objem

def obsah_kuzela(polomer,polomer_plasta):
    obsah = vypocitaj_pi(1000) * polomer(polomer_plasta + polomer)
    return obsah

polomer = float(input("Zadaj polomer kužeľa : "))
polomer_plasta = float(input("Zadaj polomer plášťa kužeľa: "))
vyska = float(input("Zadaj výšku kužeľa : "))

print(f"Objem kužeľa je : {objem_kuzela(polomer,vyska)}")
print(f"Obsah kvádra je : {objem_kuzela(polomer,polomer_plasta)}")
