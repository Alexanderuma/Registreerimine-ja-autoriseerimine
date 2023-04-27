import re
import random

def pass_Check():
    '''Функция проверяет пароль на соответсвие и правильность условий. Универсальная, поэтому пепеиспользуется в несколькими функциями одновременно, в модуле: MyModule.py '''

    print("Пароль должен состоять минимум из 8 символов и содержать в себе 1 цифру, 1 большую и маленькую букву, и 1 спецсимвол")
    while (True):
                
        print()
        password = input("Придумай надежный пароль: ")

        if len(password) < 8:
            while (True):
                print('Пароль должен состоять минимум из 8 символов')
                break
        elif re.search('[0123456789]', password) is None:
            print('В пароле нет цифр')
        elif re.search('[qwertyuiopasdfghjklzxcvbnm]', password) is None:
            print('В пароле нет букв в нижнем регистре')
        elif re.search('[QWERTYUIOPASDFGHJKLZXCVBNM]', password) is None:
            print('В пароле нет букв в верхнем регистре')
        elif re.search('[@$^=.,:;!_*-+()/#¤%&]', password) is None:
            print('В пароле нет спецсимволов')
        else:
            print()
            print('Ваш пароль надежный')
            break
    
    return password


def password_AutoGeneration(log:list, pas:list):     
    '''Функция автоматически генерирует рандомный пароль.'''
    #### Её пришлось вынести в отделный модуль, так как она не хотела работать в одном модуле: MyModule.py вместе с основной фунцией: def registration()

    str0="@$^=.,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0+str1+str2+str3
    
    ls = list(str4)
    
    random.shuffle(ls)
    
    psword = ''.join([random.choice(str0) for x in range(2)]) + ''.join([random.choice(str1) for x in range(2)]) + ''.join([random.choice(str2) for x in range(2)]) + ''.join([random.choice(str3) for x in range(2)])
    
    passDemo = list(psword)
    random.shuffle(passDemo)
    passMixed = ''.join(passDemo)
    
    pas.append(passMixed)
    
    print()
    print(f"Ваш сгенерированный пароль: {passMixed} Запомните его!")
    print("Регистрация завершена.")