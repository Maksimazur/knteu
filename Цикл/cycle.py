correct_choice = False
while not correct_choice:
    choice = input("Введіть число 1 або 2:")
    if choice == "1" or choice == "2":
        correct_choice = True
    else:
        print ("Неправильно введено число, повторіть введеня")