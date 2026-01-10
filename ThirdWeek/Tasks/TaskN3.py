# Напишите программу, создающую список из чисел, которые при делении на 5 дают в остатке 3. Отобразить этот список в обратном порядке
rangeOfIterations = int(input("Enter the number up to which you want to calculate: "))
listOfDigits = []
for i in range(rangeOfIterations + 1):
    if i % 5 == 3:
        listOfDigits.append(i)

print(sorted(listOfDigits, reverse=True))

