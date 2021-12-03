import pylab

txt = '''Да уж... Это будет. Очень долго. Нет, серьезно скольо еще ждать? Я уже устал, понимаешь? Сил нет!'''

sent = ['?', '!', '...']

xdata = []
ydata = []

for i in sent:
    a = txt.count(i)
    ydata.append(a)
    

for i in range (3):
    xdata.append(i+1)

sent.insert(0, 0)
xdata.insert(0, 0)
pylab.xticks(range(len(xdata)), sent)
xdata.remove(0)

pylab.title('Задача 7.3')
pylab.bar (xdata, ydata)
pylab.show()