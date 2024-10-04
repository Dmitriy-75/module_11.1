
'Тест библиотеки Request'

import requests
r = requests.get('https://zaycev.net/genres/index.html')
print(r.headers)
print(r.text)
print(r.headers['content-type'])
print(r.encoding)
print(r.json)
print(r.url)
payload = dict(key1='value1', key2='value2')
r = requests.post('https://zaycev.net/genres/index.html', data=payload)
# print(r.text)


'Тест библиотеки Pillow'

from PIL import Image
#
with Image.open("1246514040_hiop_ru_cats_04.jpg") as im:
    a= im.rotate(45).show()                   # переворот картинки
    im.crop((100, 100, 200, 200)).show()      # обрезка картинки
print(a)
print(im)

q = Image.new('RGB',[100,100],0)  #  Черный квадрат  - Малевич
q.save('square.jpg', 'jpeg')
print(q)



'Тест библиотеки Numpay'

import numpy

a=numpy.ones(8)                        #создание единичной матрицы
b= numpy.array([1,2,3,4,5,6,7,8])      #создание матрицы чисел b
c = b.reshape(4, 2)                    #преобразование размерности матрицы b
d=b[3:8]                               #срез матрицы

print(a)
print(b)
print(c)
print(d)









