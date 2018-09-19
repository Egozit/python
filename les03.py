
import os
import psutil


answer = input("Хотите поработать? (Y/N)")

if answer == "Y":
    print("Отлично, за работу!")
    print("Я умею: ")
    print(" [1] - выведу список файлов")
    print(" [2] - выведу информацию о системе")
    print(" [3] - выведу список процессов")
    do = int(input("Укажите номер действия: "))
    
    if do == 1:
        print(os.listdir())
    elif do == 2:
        pass
    elif do ==3:
        print(psutil.pids())
    else:
        pass
        
elif answer == "N":
    print("Прощайте!")
else:
    print("Неизвестный ответ!")