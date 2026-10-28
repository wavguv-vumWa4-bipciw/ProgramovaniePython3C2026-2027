globalna_ip_adresa_databazy = "192.168.1.1"

def moja_funkcia():
    print(f"IP adresa SQL servera je : {globalna_ip_adresa_databazy}")

moja_funkcia()
print(f"IP adresa SQL servera je : {globalna_ip_adresa_databazy}")

def set_ip_addresu(nova_ip):
    global globalna_ip_adresa_databazy#global - chcem modifikovať glob. prem.
    globalna_ip_adresa_databazy = nova_ip

set_ip_addresu("192.168.2.1")
moja_funkcia()

konfiguracia = {
    "ip_adresa" : "192.168.1.1",
    "uzivatel" : "admin",
    "heslo" : "admin"
}

print(konfiguracia)
def zobraz_konfiguraciu():
    global konfiguracia
    print(konfiguracia)

def vypocet_faktorial():
    hodnota = int(input("Zadaj hodnotu pre výpočet faktoriálu : "))
    vysledok = 1
    for i in range(1,hodnota+1):
        vysledok *= i
    print(f"Hodnota faktoriálu je : {vysledok}")

vypocet_faktorial()


