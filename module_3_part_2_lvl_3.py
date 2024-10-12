print ("Модуль 3, Часть 2, Уровень 2")
d = {'name1' : 'idl', 'name2' : 'id2', 'name3' : 'id3'}
print("Исходный словарь - ", d)
name = []
id = []
for names, ids in d.items() :
    name.append(names)
    id.append(ids)
for i in range(len(name)) :
    d[id[i]] = name[i]
    del d[name[i]]
print("Полученный словарь - ", d)