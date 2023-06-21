n = int(input())
a = 0 #the first quarter
b = 0 #the second quarter
c = 0 #the third quarter
d = 0 #the fourth quarter
while n > 0:
    stroka = input()
    qw = [int(i) for i in stroka.split()]
    if qw[0] > 0:
        if qw[1] > 0:
            a += 1
        elif qw[1] < 0:
            d += 1
    elif qw[0] < 0:
        if qw[1] > 0:
            b += 1
        elif qw[1] < 0:
            c += 1   
    n -= 1
print("Первая четверть:", a)
print("Вторая четверть:", b)
print("Третья четверть:", c)
print("Четвертая четверть:", d)