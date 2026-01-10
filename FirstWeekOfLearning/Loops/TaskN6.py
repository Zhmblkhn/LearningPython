# У пользователя запрашиваются два положительных числа X и R, причем X < R.
# Необходимо, используя цикл while вывести на экран все числа из промежутка от Х до R
# и посчитать их кол-во, X, R включительно
X = int(input("Enter first: "))
R = int(input("Enter second: "))
amount = 0

while X <= R:
    print(X, end=" ")
    amount += 1
    X += 1

print(f'\n{amount}')
