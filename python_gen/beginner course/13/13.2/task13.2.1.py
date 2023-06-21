def draw_box(fill, base):
    for i in range(1, base + 1):
        if i <= base//2 + 1:
            print(fill * i)
        else:
            print(fill * (base - i + 1))
    
fill = input()
base = int(input())
draw_box(fill, base)