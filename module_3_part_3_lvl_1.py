def area(a, b, c) :
    p = (a + b + c)/2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return S
print ("Модуль 3, Часть 3, Уровень 1")
while True :
    a = float(input("Введите последовательно длины сторон треугольника через ENTER\n"))
    if a <= 0 :
        print("Длинна стороны не может быть меньше или равной 0")
        continue
    b = float(input())
    if b <= 0 :
        print("Длинна стороны не может быть меньше или равной 0")
        continue
    c = float(input())
    if c <= 0 :
        print("Длинна стороны не может быть меньше или равной 0")
        continue
    break
print("Площадь треугольника = ", area(a, b, c))