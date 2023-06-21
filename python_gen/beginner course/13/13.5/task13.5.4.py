# объявление функции
def is_password_good(password):
    flag = False
    count_upper = 0
    count_lower = 0
    count_num = 0
    if len(txt) >= 8:
        for i in txt:
            if 65 <= ord(i) <= 90:
                count_upper += 1
            elif 97 <= ord(i) <= 122:
                count_lower += 1
            elif 48 <= ord(i) <= 57:
                count_num += 1
    if count_lower > 0 and count_num > 0 and count_upper > 0:
        flag = True
    if flag:
        return True
    else:
        return False
        

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))