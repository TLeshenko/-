x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))

# Проверяем в какой четверти лежит точка
if x > 0 and y > 0:
    print("Точка находится в первой четверти")
elif x < 0 and y > 0:
    print("Точка находится во второй четверти")
elif x < 0 and y < 0:
    print("Точка находится в третьей четверти")
elif x > 0 and y < 0:
    print("Точка находится в четвёртой четверти")
elif x == 0 and y != 0:
    print("Точка лежит на оси Oy")
elif x != 0 and y == 0:
    print("Точка лежит на оси Ox")
else:
    print("Точка находится в начале координат")