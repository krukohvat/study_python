eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


while True:
    meth = input("Encryption or decryption? E/D:").lower()
    if meth == "e" or meth == "d":
        break
    else:
        print("Input E for Encryption or D for Decryption")


while True:
    lang = input("Choose language - E or R:").lower()
    if lang == "e":
        step = int(input("Input step value (1-25):"))
        power = 26
        break
    elif lang == "r":
        step = int(input("Input step value (1-31):"))
        power = 32
        break
    else:
        print("Input E for English or R for Russian")


text = input("Input text for our task:")
res = []


for i in text:
    if i.lower() != i.upper():
        if meth == 'e':
            if i == i.lower():
                asd += [chr((ord(i)-ord('a')+k)%25)]
            else:
                res += [chr(ord(i)+step)]
        elif meth == "d":
            res += [chr(ord(i)+step)]
    else:
        res += [i]
        
        
       asd += [eng_lower_alphabet[(wor.find(i)+k)%25]]