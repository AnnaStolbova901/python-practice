# Odkaz na zadání: https://kodim.cz/czechitas/uvod-do-progr-2/uvod-do-programovani-2/uvod/priklady/rodna-cisla

rodna_cisla = [
    "845128/6219",
    "801002/5021",
    "900116/8291",
    "790501/7894",
    "850706/9259",
    "891222/1824",
    "870327/9582",
    "810602/6883",
    "850512/5070",
    "790531/7081"
]

zena = 0
muz = 0

for cislo in rodna_cisla:
    if cislo[2] == "0":
        muz += 1
    elif cislo[2] == "1":
        muz += 1
    else:
        zena += 1

print(f"Do ordinace přišel počet mužů: {muz} a počet žen: {zena}. ")

rok = 0
mesic = 0
den = 0

for cislo in rodna_cisla:
    if int(cislo[0] + cislo[1]) > rok:
        rok = int(cislo[0] + cislo[1])
        mesic = int(cislo[2] + cislo[3])
        if mesic > 50:
            mesic -= 50
        den = int(cislo[4] + cislo[5])
    elif int(cislo[0] + cislo[1]) == rok:
        if int(cislo[2] + cislo[3]) > mesic:
            mesic = int(cislo[2] + cislo[3])
            if mesic > 50:
                mesic -= 50
            den = int(cislo[4] + cislo[5])
        elif int(cislo[2] + cislo[3]) == mesic:
            if int(cislo[4] + cislo[5]) > den:
                den = int(cislo[4] + cislo[5])
print(f"Nejmladší pacient se narodil {den}. {mesic}. 19{rok}.")

rok2 = 99
mesic2 = 12
den2 = 31

for cislo in rodna_cisla:
    if int(cislo[0] + cislo[1]) < rok2:
        rok2 = int(cislo[0] + cislo[1])
        mesic2 = int(cislo[2] + cislo[3])
        if mesic2 > 50:
            mesic2 -= 50
        den2 = int(cislo[4] + cislo[5])
    elif int(cislo[0] + cislo[1]) == rok2:
        if int(cislo[2] + cislo[3]) < mesic2:
            mesic2 = int(cislo[2] + cislo[3])
            if mesic2 > 50:
                mesic2 -= 50
            den2 = int(cislo[4] + cislo[5])
        elif int(cislo[2] + cislo[3]) == mesic2:
            if int(cislo[4] + cislo[5]) < den2:
                den2 = int(cislo[4] + cislo[5])
print(f"Nejstarší pacient se narodil {den2}. {mesic2}. 19{rok2}.")
    