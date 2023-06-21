# объявление функции
def is_correct_bracket(text):
    ls=[]
    flag = True
    count_open = 0
    count_close = 0
    for i in txt:
        ls.append(i)
    if ls[0] == "(" and ls.count("(") == ls.count(")"):
        for j in range(len(ls)):
            if ls[j] == "(":
                count_open += 1
            else: 
                count_close += 1
            if count_close > count_open:
                flag = False
                break  
    else:    
        flag = False
    if flag:
        return True
    else:
        return False
# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))