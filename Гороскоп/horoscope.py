prodolzhit = 'y'
while prodolzhit == 'y': 
    yourname = input("Введите ваше имя: ")
    yourgender = False
    while not yourgender:
        gender = input("Какой ваш пол? (введите М или Ж):")
        if gender == "М" or gender == "Ж":
            yourgender = True
        else:
            print ("Введите М или Ж!!!")
    month = input("Введите ваш месяц рождения (число с 1 до 12): ")
    day = int(input("Введите ваше день рождения (число с 1 до 31): "))
    if month == "1" and day <= 20 and day >= 1 or month == "12" and day <= 31 and day >= 22:
        print (yourname, ", вы - Козерог!")
    elif month == "1" and day <= 31 and day >= 21 or month == "2" and day <= 18 and day >= 1:
        print (yourname, ", вы - Водолей!")
    elif month == "2" and day <= 29 and day >= 19 or month == "3" and day <=20 and day >= 1:
        print (yourname, ", вы - Рыбы!")
    elif month == "3" and day <= 31 and day >= 21 or month == "4" and day <= 20 and day >= 1:
        print (yourname, ", вы - Овен!")
    elif month == "4" and day <= 30 and day >= 21 or month == "5" and day <= 21 and day >= 1:
        print (yourname, ", вы - Телец!")
    elif month == "5" and day <= 31 and day >= 22 or month == "6" and day <= 21 and day >= 1:
        print (yourname, ", вы - Близнецы!")
    elif month == "6" and day <= 30 and day >= 22 or month == "7" and day <= 22 and day >= 1:
        print (yourname, ", вы - Рак!")
    elif month == "7" and day <= 31 and day >= 23 or month == "8" and day <= 23 and day >= 1:
        print (yourname, ", вы - Лев!")
    elif month == "8" and day <= 31 and day >= 24 or month == "9" and day <= 23 and day >= 1:
        print (yourname, ", вы - Дева!")
    elif month == "9" and day <= 30 and day >= 24 or month == "10" and day <= 23 and day >= 1:
        print (yourname, ", вы - Весы!")
    elif month == "10" and day <= 31 and day >= 24 or month == "11" and day <= 22 and day >= 1:
        print (yourname, ", вы - Скорпион!")
    elif month == "11" and day <= 30 and day >= 23 or month == "12" and day <= 21 and day >= 1:
        print (yourname, ", вы - Стрелец!")
    else:
        print ("Некоректно введена дата рождения!")
    prodolzhit = input("Натисніть 'Y', щоб продовжити, або будь яку іншу клавішу, щоб вийти")