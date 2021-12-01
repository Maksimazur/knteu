file = open("HarryPotter.txt", "rt")
a = 0
b = 0
for line in file:
  a += len(line) - line.count(' ')
  b += len(line)
file.close()
print("Символов без пробелов:", a, '\n' "Символов с пробелами:", b)

file = open("HarryPotter.txt", "rt")
d = file.read()
с = d.split()
file.close()
print('Слов:', len(с))