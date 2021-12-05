from prettytable import PrettyTable

from data import dt

x = PrettyTable()

x.field_names = ["Найменування валюти","Код валюти","Рік","Курс на 1.10","Курс на 1.11 курс крб.","Курс на 1.12 курс крб.","Рівень за три місяці"]

for i in range(0, len(dt)):
    x.add_rows(
        [
            dt[i]
        ]
    )

def openTabble():
    print('\nАНАЛИЗ ЗМІНИ ЦІН')
    print(x)