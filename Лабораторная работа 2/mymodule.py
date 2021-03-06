def lsort(l1):
   """Сортирует список от большего числа к меньшему"""
   print("Сортированный список:", sorted(l1))

def lsearch(l2):
   """Проверяет наличие заданого пользователем элемента в списке"""
   x = int(input("Введите искомый элемент: "))
   x2 = x in l2
   if x2 == True:
      print("Элемент", x, "есть в списке")
   elif x2 == False:
      print("Элемента", x, "нет в списке")

def lindex(l3):
   """Выдает индекс искомого пользователем элемента"""
   y = int(input("Введите элемент для поиска места в списке: "))
   print("Элемент", y, "находится в списке под индексом", l3.index(y,))

def l5min(l4):
   """Ищет первые пять минимальных элементов списка"""
   print ("Первые пять минимальных элементов списка:", sorted(l4)[:5])

def l5max(l5):
   """Ищет первые пять максимальных элементов списка"""
   print ("Первые пять максимальных элементов списка:", sorted(l5)[::-1][:5])

def lmean(l6):
   """Ищет среднее арифметическое чисел в списке"""
   print("Среднее арифметическое чисел в списке:", sum(l6) / len(l6))

def lrepeat(l7):
   """Создает список, сформированый из старого, но без повторов"""
   z = list(set(l7))
   print("Список без повторов:", z)