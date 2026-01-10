# Напишите программу, которая проверяет является ли введенное пользователем число четным.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"Entered number: {number} is even.")
else:
    print(f"Entered number: {number} is odd.")