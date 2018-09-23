# coding : utf-8

# комментарий

Name = "Лучшая программа в мире"

print(Name, ". Привет, программист!")

#print("10/3=" + str(10/3)) 
#print("10//3=" + str(10//3)) 
#print("10%3=" + str(10%3))
#print("10**3=" + str(10**3))  

answer = input("Хотите поработать? (Y/N)")

if answer == "Y":
	print("Получите премию!")
elif answer == "N":
	print("Прощайте!")
else:
	print("Неизвестный ответ!")