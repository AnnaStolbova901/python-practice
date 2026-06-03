# Odkaz na zadání https://kodim.cz/czechitas/uvod-do-progr-2/uvod-do-programovani-2/json/excs/skolka

import csv

data = []

with open ("data/kids.csv", encoding="utf-8") as file:
    csv_reader = csv.reader(file, delimiter= ",")
    for row in csv_reader:
        data.append(row)

classes = {}

for kid in data:
    name = kid[0]
    classroom = kid[1]
    birthday = kid[2]
    birthday_month = int(birthday.split(".")[1].strip())

    if classroom not in classes:
        classes[classroom] = {}

    if birthday_month not in classes[classroom]:
        classes[classroom][birthday_month] = []
    classes[classroom][birthday_month].append(name)


for classroom in classes:
    with open(f"data/{classroom}.txt", "w", encoding="utf-8") as file:
        file.write(f"Třída {classroom}\n")

        for month_number in sorted(classes[classroom]):
            names = classes[classroom][month_number]
            file.write(f"{month_number}: {', '.join(names)}\n")