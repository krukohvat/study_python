wasd = [int(i) for i in input()]
if len(wasd) == 5:
    while wasd[-1] == 0:
        del wasd[-1]
    print(*wasd[::-1], sep='')    
else:
    print(wasd[0], end = '')
    print(*wasd[len(wasd):-len(wasd):-1], sep='')