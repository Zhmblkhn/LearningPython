# Напишите программу, которая, получает на вход 2 числа (большее и меньшее).
# Определить, кратно ли первое число второму.
# Вывести на экран сообщение об этом, а также остаток от деления, если первое числ не кратно второму.
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number which less than first: "))
if number1 % number2 == 0:
    print("The first number is a multiple of second number")
else:
    print("The first number is not a multiple of second number")