# Напишите программу, вычисляющую сумму всех четных чисел от 0 до N (включительно).
# N - целое число, введенное пользователем.
# Для решения используйте цикл for.
N = int(input("Enter a number: "))
summ = 0

for i in range(0, N + 1):
    if i % 2 == 0:
        summ += i

print(f"Sum of all even numbers till N: {summ}")