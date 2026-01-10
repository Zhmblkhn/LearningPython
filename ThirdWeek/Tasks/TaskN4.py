# Напишите программу, которая вычисляет факториал числа
number = int(input("Enter the number:"))
total = 1
for i in range(1, number + 1):
    total *= i

print(total)