# Напишите программу, в которой создается и отображается список, содержащий степени двойки. Размер списка вводится пользователем
lengthOfList = int(input("Enter length of list: "))

listOfDegreesTwo = []

for i in range(1, lengthOfList + 1):
    listOfDegreesTwo.append(pow(2,i))
    i += 1

print(listOfDegreesTwo)