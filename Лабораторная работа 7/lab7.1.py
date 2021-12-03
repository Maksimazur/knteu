from numpy import *
import matplotlib.pyplot as plt
t = linspace(0, 5, 50)
y = cos(t**2)/t #Вариант 16
plt.plot(t, y)
plt.grid(True)
plt.title('Задача 7.1')
plt.legend(['y=cos(x**2)/x'])
plt.show()