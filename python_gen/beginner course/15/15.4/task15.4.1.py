from random import *
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
num_of_pswd = input("How many password do you want?")
length = input("How many symbols for each password do you want?:")
up_let = input("Include upercase letters? Y/N:").lower()
low_let = input("Include lowercase letters? Y/N:").lower()
sp_sym = input("Include special symbols? Y/N:").lower()
dig = input("Include numbers? Y/N:").lower()

if up_let == "y" or up_let == "yes":
    chars += uppercase_letters
if low_let == "y" or low_let == "yes":
    chars += lowercase_letters
if sp_sym == "y" or sp_sym =="yes":
    chars += punctuation
if dig == "y" or dig =="yes":
    chars += digits
print(chars)

def gen_pass(length, chars):
    pswd = ''
    for i in range(int(length)):
        pswd += choice(chars)
    print(pswd)

while True:
    for j in range(int(num_of_pswd)):
        gen_pass(length, chars)
    answ = input("Doy you want to generate new set? Y/N:").lower()
    if answ != "y" or answ != "yes":
        break