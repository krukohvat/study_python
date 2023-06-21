# на вход подается число
# программа выдает все простые числа до этого числа
n = int(input())
count = 0
num = [1, 2, 3]
for i in range(4, n+1):
    for j in range(2, i//2+1):
        if i%j == 0:
            count += 1
    if count == 0:
        num.append(i)
    else:
        count = 0
print(*num)