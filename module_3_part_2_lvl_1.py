print ("Модуль 3, Часть 2, Уровень 1")
l = [1, 4, 1, 6, "hello", "a", 5, "hello", "a"]
dubles = []
for elem in l :
    count = 0
    for i in range(len(l)) :
        if elem == l[i] :
            count +=1
        if count > 1 :
            dubles.append(elem)
print ("Исходный массив - ", l, "\nМассив повторяющихся элементов - ", list(set(dubles)))