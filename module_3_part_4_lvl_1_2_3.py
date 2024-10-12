print("Модуль 3, Часть 4, Уровень 1")
def register(login, passwd) :
    print("reg")

#def login(login, passwd) :

#def isregistred(login, passwd) :
while True :
    choice = input("Выберите желаемое действие из предложенных вариантов и введите его в консоль\n\t Вход\t Регистрация\t Выход \t\n")
    if choice == 'регистрация' or choice == 'Регистрация':
        login = input("\033[JВведите логин для регистрации\n")
        passwd = input("Введите пароль для регистрации\n")
        register(login, passwd)
        continue
    elif choice == 'вход' or choice == 'Вход' :
        login = input("\033[JВведите логин для входа\n")
        passwd = input("Введите пароль для входа\n")
        continue
    elif choice == 'выход' or choice == 'Выход' :
        break
    else :
        print("Такой вариант отсутствует, выберите из предложенных")
        continue

