# объявление функции
def is_valid_password(password):
    psw_list = psw.split(':')
    flag = True
    if len(psw_list) > 3:
        flag = False
    if psw_list[0] != psw_list[0][::-1]:
        flag = False
    psw_list[1], psw_list[2] = int(psw_list[1]), int(psw_list[2])
    if psw_list[2] % 2 != 0:
        flag = False
    for i in range(2, psw_list[1] // 2):
        if psw_list[1] % i == 0:
            flag = False
            break
    if flag:
        return True
    else:
        return False

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))