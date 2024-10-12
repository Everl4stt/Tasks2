print ("Модуль 3, Часть 2, Уровень 2")
from random import randint
n = 5
max = 0
m = [[randint(0,100) for i in range(n)] for j in range(n)]
print("Исходная матрица\n\t")
for i in range(n) :
    for j in range(n) :
        print(m[i][j],end = " ")
    print("\n")
for i in range(n) :
    for j in range(n) :
        max = (m[i][j] if m[i][j] > max else max  )
print("Максимальный элемент матрицы = ", max)