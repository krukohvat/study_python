def print_fio(name, surname, patronymic):
    print((surname[0] + name[0] + patronymic[0]).upper())

name, surname, patronymic = input(), input(), input()
print_fio(name, surname, patronymic)