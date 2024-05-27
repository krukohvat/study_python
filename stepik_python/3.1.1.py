'''https://stepik.org/lesson/3372/step/8?unit=955'''

def f(x):
    if x <= -2:
        f = 1 - (x+2)*(x+2)
    elif -2 < x <= 2:
        f = -(x/2)
    else:
        f = (x-2)*(x-2) + 1
    return f
x = float(input())
print(f(x))