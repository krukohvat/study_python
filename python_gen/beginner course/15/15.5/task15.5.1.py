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
        break
    elif lang == "r":
        step = int(input("Input step value (1-31):"))
        break
    else:
        print("Input E or R")