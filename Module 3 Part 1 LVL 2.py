print ("Модуль 3, Часть 1, Уровень 2")
while True :
    n = int(float(input("Введите число повторений n - оно должно быть целым и быть больше 1\n")))
    if  n < 1 :
        print("Вы ввели  число меньше 1")
        continue
    break
itr = 0
while itr < n :
    print("for - частный случай цикла while")
    itr = itr + 1

