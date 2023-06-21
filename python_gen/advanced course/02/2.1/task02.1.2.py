weight = float(input())
height = float(input())
imt = weight/(height**2)
if 18.5 > imt:
    print("Недостаточная масса")
elif imt > 25:
    print("Избыточная масса")
else:
    print("Оптимальная масса")