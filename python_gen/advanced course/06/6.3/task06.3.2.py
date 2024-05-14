poets = [
    ("Тургенев", 14),
    ("Есенин", 13),
    ("Маяковский", 28),
    ("Фет", 15),
    ("Лермонтов", 20),
]

for i in range(len(poets)):
    print()
    print(poets)
    for j in range(i + 1, len(poets)):
        print('i=', i, ' j=', j)
        if poets[i] > poets[j]:
            poets[i], poets[j] = poets[j], poets[i]
            print(poets)

print(poets[0])
print(poets[-1])