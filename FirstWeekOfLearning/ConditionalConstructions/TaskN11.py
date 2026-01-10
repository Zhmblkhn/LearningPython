# Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется следующее соотношение:
# сумма первой и последней цифр равна разности второй и третьей цифр.

a = int(input("Enter a number: "))
first_num = a // 1000
second_num = (a % 1000) // 100
third_num = (a % 100) // 10
fourth_num = a % 10

if first_num + fourth_num == second_num - third_num:
    print("Yes")
else:
    print("No")



