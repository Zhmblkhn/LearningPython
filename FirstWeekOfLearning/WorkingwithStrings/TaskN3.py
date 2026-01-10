# Напишите программу, которая получает на вход строку и символ.
# Определите сколько раз во введенной строке встречается введенный символ.
# Пользователь вводит строку, необходимо посчитать сколько в этой строке встречается букв "y" и "s" (в обоих регистрах).
# Ввод и проверки осуществляются на английском языке.
# Вывод должен иметь вид:
#
# Буква 'y' встречается XXXX раз
# Буква 's' встречается XXXX раз
# Если нет таких букв то:
# Во введенном предложении нет букв 'y' и 's'.

my_str = input("Enter a string: ").lower()
counter_y = 0
counter_s = 0

for ch in range(len(my_str)):
    if my_str[ch] == 'y':
        counter_y += 1
    elif my_str[ch] == 's':
        counter_s += 1

if counter_y == 0 and counter_s == 0:
    print("There is no any s and y")
else:
    print(f"Letter 'y' occurs {counter_y} times")
    print(f"Letter 's' occurs {counter_s} times")

