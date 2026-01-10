# Напишите программу, которая определяет, является число четным или нечетным.

number = int(input('Enter a number: '))
if number % 2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')