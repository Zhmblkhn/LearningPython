# Напишите программу, которая запрашивает у пользователя месяц его рождения в формате от 1 до 12.
# Необходимо определить и вывести время его года
month = int(input("Enter month when ypu born (1-12): "))

match month:
    case 1 | 2 | 12:
        print("You born in winter")
    case 3 | 4 | 5:
        print("You born in spring")
    case 6 | 7 | 8:
        print("You born in summer")
    case 9 | 10 | 11:
        print("You born in autumn")