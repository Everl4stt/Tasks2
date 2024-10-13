import json

print("Модуль 3, Часть 4, Уровень 1")
def register(login, passwd) :
    with open("data.json", "r", encoding = "utf-8") as f:
        data = json.load(f)
    if login not in data.keys() :
        data[login] = passwd
        with open("data.json", "w", encoding = "utf-8") as f:
            json.dump(data, f)
        print("Регистрация прошла успешно!")
    else :
        print("Пользователь с таким логином уже существует")

def login(login, passwd) :


#def isregistred(login, passwd) :
data = {}
with open("data.json", "w", encoding = "utf-8") as f:
    json.dump(data, f)
while True :
    choice = input("Выберите желаемое действие из предложенных вариантов и введите его в консоль\n\t Вход\t Регистрация\t Выход \t\n")
    if choice.lower() == 'регистрация' :
        login = input("Введите логин для регистрации\n")
        passwd = input("Введите пароль для регистрации\n")
        register(login, passwd)
        continue
    elif choice.lower() == 'вход' :
        login = input("Введите логин для входа\n")
        passwd = input("Введите пароль для входа\n")
        continue
    elif choice.lower() == 'выход' :
        break
    else :
        print("Такой вариант отсутствует, выберите из предложенных")
        continue

