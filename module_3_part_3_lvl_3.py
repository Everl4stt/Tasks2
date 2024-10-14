print("Модуль 3, Часть 3, Уровень 3")
n = [56, 9, 99, 99, 88]
def maxnumber(n) :
    maxnum = ""
    for i in range(len(n)) :
        n[i] = str(n[i])
    for i in range(len(n)):
        for j in range(len(n)-1) :
            if int(n[i] + n[j]) > int(n[j] + n[i]) :
                n[i], n[j] = n[j], n[i]
    for i in range(len(n)) :
        maxnum += n[i]
    return maxnum
print("Максимальное число из исходного массива: ", maxnumber(n))
