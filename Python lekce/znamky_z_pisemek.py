# Odkaz na zadání: https://kodim.cz/czechitas/uvod-do-progr-2/uvod-do-programovani-2/slicing-metody-moduly/dalsi-priklady/znamky-z-pisemek

import statistics

data = [
    ["Student", "Otázka 1", "Otázka 2", "Otázka 3", "Otázka 4"],
    ["A", 9, 7, 8, 5],
    ["B", 5, 3, 6, 6],
    ["C", 8, 4, 9, 7],
    ["D", 8, 5, 4, 8],
    ["E", 10, 6, 10, 7]
]

for student in data[1:]:
    soucet_bodu = sum(student[1:])
    if soucet_bodu >= 36:
      print(f"Student {student[0]} dostak známku 1.")
    elif soucet_bodu >= 32:
      print(f"Student {student[0]} dostak známku 2.")
    elif soucet_bodu >= 26:
      print(f"Student {student[0]} dostak známku 3.")
    elif soucet_bodu >= 20:
      print(f"Student {student[0]} dostak známku 4.")
    else:
      print(f"Student {student[0]} dostak známku 5.")

body_za_otazky = []
for otazka in data[0][1:]:
  body_za_otazky.append([otazka])

for radek in data[1:]:
  index_otazky = 0
  for bod_otazka in radek[1:]:
    body_za_otazky[index_otazky].append(bod_otazka)
    index_otazky += 1

for otazka in body_za_otazky:
    prumer = statistics.mean(otazka[1:])
    print(f"Průměr bodů u {otazka[0]} je {prumer}.")

prumery = []

for radek in body_za_otazky:
  otazka = radek[0]
  prumer = statistics.mean(radek[1:])
  prumery.append([otazka, prumer])

min_prumer = prumery[0]

for prumer in prumery:
  if prumer[1] < min_prumer[1] :
    min_prumer = prumer
print(f"Nejmenší průměr má {min_prumer[0]}.")

max_prumer = prumery[0]

for prumer in prumery:
  if prumer[1] > max_prumer[1]:
    max_prumer = prumer

print(f"Největší průmer má {max_prumer[0]}.")
  



