# Напишите программу, которая, получает на вход целое положительное число.
# Необходимо вывести все числа от 0 до N (N - это выведенное число), используя цикл while
N = int(input("Enter a number: "))
iterations = 0
while iterations <= N:
    print(iterations, end=" ")
    iterations += 1