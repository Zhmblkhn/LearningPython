# Напишите программу, которая определяет наибольшее и наименьшее из двух чисел,
# введенных пользователем
number1 = int(input("Please enter first number: "))
number2 = int(input("Please enter second number: "))
if number1 > number2:
    print("First number is greater than second number: {number1} > {number2}.")
else:
    print(f"Second number is greater than first number: {number1} < {number2}.")