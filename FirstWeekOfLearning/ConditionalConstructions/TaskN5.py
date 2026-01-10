# Напишите программу, определяющую является ли введенный пользователем год високосным
year = input("Enter year what you want: ")
if year % 4 == 0 or year % 400 == 0:
    print("The year is leap")
else:
    print("The year is not leap")