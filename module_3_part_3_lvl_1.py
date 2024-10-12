def area(a, b, c) :
    p = (a + b + c)/2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return S
a = float(input("Введите последовательно длины сторон треугольника через ENTER\n"))
b = float(input())
c = float(input())
print("Площадь треугольника = ", area(a, b, c))