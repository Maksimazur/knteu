import mymodule

#Создание списка
a=[]
n=int(input("Введите размер списка: "))
print("Введите элементы списка: ")
for i in range(n):
    a.append(int(input()))
print("Список:", a)

#Сортировка списка
mymodule.lsort(a)

#Проверка наличия элемента в списке
mymodule.lsearch(a)

#Поиск последовательности элемента в списке
mymodule.lindex(a)

#Поиск первых пяти минимальных элементов
mymodule.l5min(a)

#Поиск первых пяти максимальных элементов
mymodule.l5max(a)

#Среднее арифметическое
mymodule.lmean(a)

#Удаление повторов
mymodule.lrepeat(a)