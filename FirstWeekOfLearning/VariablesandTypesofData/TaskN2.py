# Напишите программу которая:
# 1) Запрашивает у пользователя его имя и, сохраняет введенное значение в переменную my_name;
# 2) Запрашивает у пользователя год рождения и сохраняет в переменную year_of_birth;
# 3) Вычисляет возраст и сохраняет его в переменную с именем age;
# 4) Выводит на экран тип переменных my_name, year_of_birth, age;
# 5) Выводит сообщение "Hello my name is: my_name, My age: age".
my_name = input("Enter your name: ")
year_of_birth = int(input("Enter your year of birth: "))
age = 2025 - year_of_birth
print("Used data types: ", type(my_name), type(year_of_birth), type(age))
print(f"Hello my name is: {my_name}. My age: {age}.")