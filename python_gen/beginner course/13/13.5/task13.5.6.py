# объявление функции
def is_palindrome(text):
    s = txt.lower()
    l = []
    for i in s:
        if ord(i) < 97 or (ord(i) > 122 and ord(i) < 1072) or ord(i) > 1103:
            s = s.replace(i, "")
    l.extend(s)
    return l == l[::-1]
    
# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))