# объявление функции
def is_one_away(word1, word2):
    list_txt1 = []
    list_txt2 = []
    count = 0
    if len(txt1) == len(txt2):
        for i in txt1:
            list_txt1.append(ord(i))
        for j in txt2:
            list_txt2.append(ord(j))
        for k in range(len(txt1)):
            if list_txt1[k] != list_txt2[k]:
                count += 1
        if count == 1:
            return True
        else:
            return False
    else:
        return False
    

# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))