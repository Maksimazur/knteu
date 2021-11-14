while True:
    N = []
    conec_spiska = False
    while not conec_spiska:
        dobavit = int(input("Задайте элементы списка: "))
        N.append(dobavit)
        danet = False
        while not danet:
            choice = input("Продолжить добавлять элементы в список? (y/n)")
            if choice == "y":
                conec_spiska = False
                danet = True
            elif choice == "n":
                conec_spiska = True
                danet = True
            else:
                print ("Введите 'y' или 'n'!")
    N.sort()
    print(N)
    i = 0
    while i < 10:
        if N[i] < 0 and index == -1:
            index = i 
        elif N[i] < 0 and N[i] > N[index]:
            index = i
    print("Максимальное отрицательное число: ",index+1, ':', N[index])