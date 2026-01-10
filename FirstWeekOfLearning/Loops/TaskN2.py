# Напишите программу, которая получает на вход целое положительное число с клавиатуры.
# Необходимо используя цикл while, вывести кол-во четных цифр в этом числе и их сумму
N = int(input("Enter a number: "))
amountOfEvenNumbers = 0
sumOfEvenNumbers = 0
while N > 0:
    digit = N % 10          # берем последнюю цифру
    if digit % 2 == 0:      # проверяем четность цифры
        amountOfEvenNumbers += 1
        sumOfEvenNumbers += digit
    N //= 10

print(amountOfEvenNumbers)
print(sumOfEvenNumbers)