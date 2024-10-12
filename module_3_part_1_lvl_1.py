print("Модуль 3, Часть 1, Уровень 1")
while True:
    x = float(input("Введите сумму вклада с клавиатуры\n"))
    if (x <= 0) :
        print ("Сумма вклада не может быть равной или меньше 0\n")
        continue
    p = float(input("Введите процент по вкладу с клавиатуры\n"))
    if (p <= 0) :
        print ("Проценты по кладу не могут быть равными или меньше 0\n")
        continue
    y = float(input("Введите сумму цели с клавиатуры\n"))
    if (y <= 0) or (y < x) :
        print ("Сумма цели не может быть равной или меньше 0 и суммы вклада\n")
        continue
    break
target = x
count = 0
while target < y :
    target = float(int(target + target *  (p / 100) ))
    count = count + 1
print("Сумма вклада станет не меньше суммы цели через ",count, " лет." )




