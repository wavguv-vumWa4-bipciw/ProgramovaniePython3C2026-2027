meno = "Fifko"
vek = 65
Oznam = "Pozor zajtra !"

print("Ahoj %s !, máš %d a v pošte máš %s" % (meno, vek,Oznam))
retazec = "Ahoj %s !, máš %d a v pošte máš %s" % (meno, vek,Oznam)
print(retazec)

retazec2 = "Ahoj {} !, máš {} a v pošte máš {}".format(meno, vek,Oznam)
print(retazec2)

retazec3 = f"Ahoj {meno} !, máš {vek} a v pošte máš {Oznam}"
print(retazec2)

#neoptimalizované spájanie reťazcov - nepoužíva sa, veľa pamäťových operácii
retazec4 = "Ahoj "+ meno +"!, máš " + str(vek) + " a v pošte máš " + Oznam
print(retazec4)

zdvojim_meno = meno * 2
print(zdvojim_meno)
print(f"Koľko znakov má premenná 'zdvojim_meno' {len(zdvojim_meno)}")
print(f"Všetko veľké písmená {zdvojim_meno.upper()}")
print(f"Všetko malé písmená {zdvojim_meno.lower()}")

text = "Ahoj svet"
print(text.replace("svet", "Fifko"))

veta = 'Nechcem crack-ovať, Fifko zakázal'
slova = veta.split()
print(slova)

nova_veta = ""
for slovo in veta:
    nova_veta += " ".join(slovo)
print(nova_veta)

nova_veta2 = " ".join(slova)
print(nova_veta2)

import math
print(f"Hodnota PI na 3 desatinné miesta {math.pi:.3f}")
print("Hodnota PI na 3 desatinné miesta %.3f" % math.pi)
print("Hodnota PI na 3 desatinné miesta {:.3f}".format(math.pi))

text = "Python"
print(f"{text:<10}")
print(f"{text:>10}")
print(f"{text:^10}")

cislo = 55
print(f"{cislo:08}")

