from MyModule import*
from UniversalFunctionsModule1 import*

loginsList = ['Alex','Max','Tom']
passwordsList = ['asdf123','123Abc!*','C0rt37!!']

while (True):
    print()
    print("******")
    print("1 - registreerimine,\n2 - autoriseerimine,\n3 - nime või parooli muutmine,\n4 - unustanud parooli taastamine,\n5 - lõpetamine")
    print()

    v = input()

    if v=='1':        
        print("---Registreerimine---")
        registration(loginsList, passwordsList)

    elif v=='2':
        print("---Autoriseerimine---")
        authorization(loginsList, passwordsList)

    elif v=='3':
        print("---Nime või parooli muutmine---")
        nameOrPassword_Change(loginsList, passwordsList)

    elif v=='4':
        print("---Unustanud parooli taastamine---")
        reinstate_Pass()

    elif v=='5':
        print("Выход.")
                
        break
    
    elif v=='6':
        print(loginsList)
        print(passwordsList)

    else:
        print("Выберите правильное действие.")

