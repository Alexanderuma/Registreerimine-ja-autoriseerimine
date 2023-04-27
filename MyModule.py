from UniversalFunctionsModule1 import*

def registration(log:list, pas:list):
    '''Функция запрашивает Логин и Пароль у пользователя и записывает эту информацию в списки логинов и паролей.
    Функция одновременно проверяет пароль, введенный пользователем, при помощи функции pass_Check() или дает возможность сгенерировать пароль автоматически, при помощи функции password_AutoGeneration().'''

    #### 2 последнии функции пришлось спрятать в модуль: UniversalFunctionsModule1.py 

    print("Введи имя и пароль ниже.")

    name=input("Имя/Логин: ")
        

    print("Придумайте пароль сами или сгенерировать его автоматически?")
    passGeneration = input("Выберите: 1 - Придумаю, 2 - Генерировать автоматически: ")

    if passGeneration == '1':
    
        securityPas = pass_Check()
        pas.append(securityPas)
        log.append(name)

        print(f"Ваш пароль: {securityPas} Запомните его. Вы прошли регистрацию!")
    
        print() # otstup

    elif passGeneration == '2':

        password_AutoGeneration(log, pas)
        log.append(name)
    
    return log, pas

def authorization(log:list, pas:list):
    '''Функция авториризируящая пользователя.
    Ищет в списке имя пользователя. Затем определяя индекс имени, ищет под тем же индексом пароль пользователя и сверяет введенный пароль, с тем, что имеется в списках паролей. Если имя и пароль пользователя совпадает с именем и паролем имеющемся в списках. То функция подтверждает авторизацию.'''

    count1 = 0 # Счетчики
    count2 = 0 

    while count1 < 3:
        print()
        name = input("Введите логин: ")

        try:
            n = log.index(name)
            findName = log[n]
            if name == findName:
                print("Правильный логин. Следуйте дальнейшим указаниям.")

                while count2 < 3:
                    print()
                    password = input("Введите пароль: ")

                    try:
                        n = pas.index(password)
                        findPass = pas[n]
                        if password == findPass:
                            print("Вы авторизированы!")
                        break    

                    except:
                        attempt_list = ['попыток','попытка','попытки']
                        num = 2-count2
                        attempts = attempt_list[num]
                        print("Неправильный пароль!")
                        print(f"Попробуйте ввести еще раз. У вас осталось еще {num} {attempts} ")
                        count2 +=1
                    if count2 == 3:
                        print("Колличество попыток закончилось! Вы не прошли авторизацию!")
                    continue           
                break
                        
                    
        except:
            print("Пользователь под таким логином не зарегистрирован.")
            count1 +=1


def nameOrPassword_Change(log:list, pas:list):
    '''Функция позволяет поменять имя или пароль пользователя'''
    while (True):
        print()
        print("Поменять имя - 1 \nПоменять пароль - 2 \nВыход - 3")
        print()
        task = input("Введите номер действия: ")

        if task == '1':
            try:
                oldLogin = input("Введите старое имя: ")
                nameIndex = log.index(oldLogin)
        
                log.remove(oldLogin)
                
                print()
                newLogin = input("Новое имя/логин: ")
                log.insert(nameIndex, newLogin)
                print()
                print(f"Замена Вашего старого имени: {oldLogin} на новое имя: {log[nameIndex]} выполнена.")
                    
            except:
                print("Вы ввели неверное имя.")

        elif task == '2':
            try:
                print()
                oldPassword = input("Введите старый пароль: ")
                passIndex = pas.index(oldPassword)
                               
                print()
                newPass = input("Новый пароль: ")
                newPass = pass_Check()
                pas.pop(passIndex)
                pas.insert(passIndex, newPass)
                           
                print()
                print(f"Замена Вашего старого пароля: {oldPassword} на новый: {pas[passIndex]} произведена.")

            except:
                print("Вы ввели неправильный пароль.")


        elif task == '3':
            print("Выход в основное меню.")
            break
            
        else:
            print()
            print("Вы выбрали неправильную задачу")
            print("Выход в основное меню.")
            break


def reinstate_Pass ():
    '''Функия, имитируящая восстановление пароля'''
    
    while (True):
        print()
        print("Вы забыли свой пароль и хотите восстановить?")
        print("Выберите: 1 - да, 0 - нет")
        action = input("Ваш выбор: ")

        if action == '1':

            print("Введите свой эмейл ниже. Ссылка и интсрукция с восстановлением придет к Вам.")
            email = input("Ваш эмейл: ")

            print()
            print(f"Ссылка и инструкция восстановления пароля выслана Вам на эмейл: {email}")
            break

        elif action == '0':
            print()
            print("Выход в основное меню.")
            break

