while True:
    a = int(input("Введіть перше число: "))
    b = int(input("Введіть друге число: "))
    z = input("Що ви бажаете зробити? ")
    if z == "+":
        print("Cума: ", a + b)
    if z == "-":
        print("Різниця: ", a - b)
    if z == "*":
        print("Добуток: ", a * b)
    if z == "/":
        print("Частка: ", a / b)