poets = [
    ("Есенин", 13),
    ("Тургенев", 14),
    ("Маяковский", 28),
    ("Лермонтов", 20),
    ("Фет", 15),
]

for i in range(len(poets)):
    print()
    print(poets)
    for j in range(i + 1, len(poets)):
        print('i=', i, ' j=', j)
        if poets[i][1] > poets[j][1]:
            poets[i], poets[j] = poets[j], poets[i]
            print(poets)

print(poets[0])
print(poets[-1])