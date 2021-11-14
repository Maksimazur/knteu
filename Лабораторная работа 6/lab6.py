import requests
from bs4 import BeautifulSoup

#Ввод ссылки на сайт
site = input("Ваш сайт: ")
r = requests.get(site)
page = BeautifulSoup(r.text, 'html.parser')
print (page.head.title.text)

#Поиск тэга
htmltag = input("Введите желаемый HTML-тэг: ")
tag_list = page.findAll(htmltag)
print ('Количевство таких тэгов:', len(tag_list))

#Поиск слова
htmlword = input("Введите желаемое слово: ")
text_list = page.findAll(text=lambda text: text and htmlword in text)
print ('Количевство таких слов:', len(text_list))

#Количевство ссылок
a_list = page.findAll('a')
print('Количевство ссылок:', len(a_list))

#Количевство картинок
img_list = page.findAll('img')
print('Количевство картинок:', len(img_list))