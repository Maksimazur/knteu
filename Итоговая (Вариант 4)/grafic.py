import matplotlib.pyplot as plt

funt = [565.46, 604.57, 1003.17, 110.25, 1120.60, 1350.40, 1350.40, 1370.10, 1380.15]
frank = [113.03, 122.60, 200.38, 250.45, 260.45, 275.20, 280.10, 283.40, 285.10]
German = [285.10, 252.07, 412.02, 444.23, 465.40, 470.20, 475.23, 480.30, 485.20]
year = ["2003","2003","2003", "2004","2004","2004","2005","2005","2005" ]

plt.plot(year,funt,label = "1 англійський фунт стерлінг")
plt.plot(year,frank,label = "1 англійський фунт стерлінг")
plt.plot(year,German,label = "1 німецька марка")
plt.xlabel("Рік")
plt.ylabel("Ціна")
plt.legend(loc='upper left')
plt.grid(True)

def showplot():
    plt.show()