import csv
import sys
import linecache

print("1 - чтение файла",'\n' "2 - запись в файл",'\n'  "3 - дозапись в файл",'\n' "4 - поиск файла в каталоге и поиск данных в файле",'\n' "5 - сортировка данных в файле")
z = input("Что вы желаете сделать? ")

if z == "1":
    stud = input("Введите имя текстового файла: ")
    txt = ".txt"
    filename = stud + txt
    fd1 = open(filename, "r", encoding="utf8")
    reader = csv.reader(fd1, delimiter="\t")
    for row in reader:
        print(row)
    fd1.close()

elif z == "2":
    stud = input("Введите имя текстового файла: ")
    txt = ".txt"
    filename = stud + txt
    fd2 = open(filename, "w", encoding="utf8")
    n=int(input("Введите количевство студентов: "))
    print("Введите оценки и имена студентов с этими оценками: ")
    for i in range(n):
        fd2.write(input() + '\t' + input() + '\n')
    fd2.close()

elif z == "3":
    stud = input("Введите имя текстового файла: ")
    txt = ".txt"
    filename = stud + txt
    fd3 = open(filename, "a", encoding="utf8")
    n=int(input("Введите количевство студентов: "))
    print("Введите оценки и имена студентов с этими оценками: ")
    for i in range(n):
        fd3.write(input() + '\t' + input() + '\n')
    fd3.close()

elif z == "4":
    stud = input("Введите имя текстового файла: ")
    txt = ".txt"
    filename = stud + txt
    whatread = int(input("Введите номер искомой строки: "))
    line = open(filename, encoding="utf8").readlines()[whatread]
    print (line)

elif z == "5":
    stud = input("Введите имя текстового файла: ")
    txt = ".txt"
    filename = stud + txt
    lines = open(filename, encoding="utf8").readlines()
    print (lines.sort())