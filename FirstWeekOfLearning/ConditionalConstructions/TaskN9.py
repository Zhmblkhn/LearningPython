# Напишите программу, которая определяет, разрешён ли пользователю доступ к интернет-ресурсу или нет.

age = int(input("Enter your age: "))
if age <= 17:
    print("Доступ запрещен")
else:
    print("Доступ разрешен")


# Напишите программу, которая определяет наименьшее из двух чисел.

first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))

if first_num > second_num:
    print(second_num)
else:
    print(first_num)
