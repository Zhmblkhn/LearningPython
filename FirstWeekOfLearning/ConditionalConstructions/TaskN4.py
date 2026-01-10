# Напишите программу, которая, получает на вход три числа.
# Выведите сумму наибольшего и наименьшего из трех чисел
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
smallestNumber = 0
largestNumber = 0


if number1 < number2 and number1 < number3:
    smallestNumber = number1
    print(f"The smallest number is {number1}")
elif number2 < number1 and number2 < number1:
    largestNumber = number2
    print(f"The smallest number is {number2}")
elif number3 < number1 and number3 < number2:
    smallestNumber = number3
    print(f"The smallest number is {number3}")

if number1 > number2 and number1 > number3:
    largestNumber = number1
    print(f"The largest number is {number1}")
elif number2 > number1 and number2 > number3:
    largestNumber = number2
    print(f"The largest number is {number2}")
elif number3 > number1 and number3 > number2:
    largestNumber = number3
    print(f"The largest number is {number3}")

print(f"Sum of smallest and largest numbers: {smallestNumber + largestNumber}")
