# объявление функции
def convert_to_python_case(text):
    ls=[]
    for i in txt:
        ls.append(i)
    for j in range(1, len(ls)):
        if 65 <= ord(ls[j]) <= 90:
            ls[j] = ls[j].lower()
            ls.insert(j, "_")
    a = ''.join(ls)
    return a.lower()

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))