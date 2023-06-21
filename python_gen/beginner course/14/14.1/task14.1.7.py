# объявление функции
def is_pangram(text):
    for i in range(97,123):
        if not chr(i) in text.lower():
            return False
    return True
        
# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))