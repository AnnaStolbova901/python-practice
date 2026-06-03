# Odkaz na zadání https://kodim.cz/czechitas/uvod-do-progr-2/uvod-do-programovani-2/slicing-metody-moduly/dalsi-priklady/hraci-2

data = [
    ["C2-P4-C4-H4-H5-C7-H8-P9", "T2-P3-H3-C6-T7-H7-T8-C9", "P2-H2-C3-T4-P5-H6-T9-H9"],
    ["C2-C4-H4-C5-C6-P7-P8-P9", "P2-C3-T4-H6-C7-C8-H8-C9", "H2-T3-H3-H5-T6-H7-T8-T9"],
    ["P2-P3-C3-H4-H5-P6-T6-T8", "T2-H2-H3-P5-P7-C7-H8-P9", "C2-C5-T5-C6-H6-T7-T9-H9"],
    ["T2-H3-H4-P6-H6-C8-T8-C9", "P2-C4-C5-T5-P7-C7-H7-H8", "P3-C3-T3-H5-C6-T7-P8-H9"],
    ["T2-P3-P4-C5-T5-H6-C9-T9", "C2-C4-P5-P6-C6-H7-T8-H8", "H2-C3-H3-H4-T6-C7-T7-P9"],
    ["C2-C3-P4-H4-C6-T7-C8-T8", "P2-T3-C4-T6-H6-P7-C7-C9", "T2-H2-C5-T5-P6-H7-H8-H9"],
    ["P2-H3-T4-H4-C6-T7-H8-H9", "C2-T2-H2-T3-C5-H5-P7-C7", "P3-C3-C4-P6-T6-H7-T8-P9"],
    ["T2-T4-H4-P5-T5-C7-P8-H8", "H2-P3-C3-H3-H5-T7-C8-P9", "P4-C4-C5-T6-P7-C9-T9-H9"],
    ["H5-P6-T6-H6-T7-H7-C8-T8", "P2-H2-C4-P5-C6-P7-P8-H8", "T2-P3-C3-T3-P4-P9-C9-H9"],
    ["T3-P4-T4-H4-C5-C6-P7-H7", "C2-T5-H5-P6-P8-C8-P9-H9", "P2-H2-C3-C4-P5-T6-T8-C9"],
]

for radek in data:
    for hrac in radek:
        clear = ""
        for znak in hrac:
            if znak.isdigit():
                if znak not in clear:
                    clear += znak
        i = radek.index(hrac)
        radek[i] = clear

vysledek = []

for radek in data:

    novy_radek = []

    for hrac in radek:
        soucet = 0
        retezec = ""
        for znak in hrac:
            if retezec == "":
                retezec = znak
            elif int(retezec[-1]) + 1 == int(znak):
                retezec += znak
            else:
                if len(retezec) >= 3:
                    for znak2 in retezec:
                        soucet += int(znak2) 
                retezec = znak
        if len(retezec) >= 3:
            for znak2 in retezec:
                soucet += int(znak2)
        novy_radek.append(soucet)
    if len(vysledek) == 0:
        vysledek.append(novy_radek)
    else:
        predchozi = vysledek[-1]
        soucet_radku = []
        i = 0
        for prvek in novy_radek:
            soucet_radku.append(predchozi[i] + prvek)
        vysledek.append(soucet_radku)
print(vysledek)
