"""
На вход программе подаётся натуральное число. Напишите программу, которая вставляет в заданное число запятые в соответствии со стандартным американским соглашением о запятых в больших числах.
"""
ch = int(input())
sp = []
if ch >= 1000:
    while ch//1000 > 0:
        if ch%1000 > 100:
            sp.append(ch%1000)
        else:
            if ch%1000 >= 10:
                sp.append(ch%1000)
                sp[len(sp)-1] = '0'+str(sp[len(sp)-1])
            else:
                sp.append(ch%1000)
                sp[len(sp)-1] = '00'+str(sp[len(sp)-1])
        ch = ch//1000
    sp.append(ch)
    sp = sp[::-1]
    print(*sp, sep=',')
else:
    print(ch)