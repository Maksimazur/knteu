class library():
 def GPA(self, name, author, year, genre, number) :
    self.name = name
    self.author = author
    self.year = year
    self.genre = genre
    self.number = number
    print("Книга №", self.number, "\t", self.name, self.author, self.year, self.genre)

s1 = library()
s2 = library()
s3 = library()
s1.GPA('Кобзар','Шевченко','1840','Поэзия',1)
s2.GPA('Евгений Онегин','Пушкин','1825','Роман',2)
s3.GPA('Собака Баскервилей','Дойл','1902','Детекив',3)

array = [s1, s2, s3]

while True:
    print("1 - поиск книг",'\n' "2 - добавить книгу")
    z = input("Что вы желаете сделать? ")

    if z == "1":
        search = input("По какому параметру вы хотите найти книгу? (название, год, автор, жанр, номер) ")
        if search == "название":
            n = input("Введите название: ")
            for i in array:
                if i.name == n:
                    print("Книга с таким название есть")
        if search == "год":
            n = input("Введите год: ")
            for i in array:
                if i.year == n:
                    print("Книга с таким годом есть")
        if search == "автор":
            n = input("Введите имя автора: ")
            for i in array:
                if i.author == n:
                    print("Книга от этого автора есть")
        if search == "жанр":
            n = input("Введите жанр: ")
            for i in array:
                if i.author == n:
                    print("Книга этого жанра есть")
        if search == "номер":
            n = input("Введите номер: ")
            for i in array:
                if i.author == n:
                    print("Книга с этим номером есть")

    elif z == "2":
        new = input("Введите имя обьекта для класса: ")
        newname = input("Введите имя книжки: ")
        newauthor = input("Введите имя автора: ")
        newyear = input("Введите год публикации книги: ") #Happy New Year! :)
        newgenre = input("Введите жанр книжки: ")
        newnumber = input("Введите порядковый номер книжки: ")
        new = library()
        new.GPA(newname, newauthor, newauthor, newgenre, newnumber)
        array.append(new)