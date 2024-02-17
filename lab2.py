#Задача 1
a = input('Введите ваше ФИО через пробел')
names =a.split()
b = ('Ваша фамилия:')
c = ('Ваше имя:')
d = ('Ваше отчество:')
print(b, names[0])
print(c, names[1])
print(d, names[2])
#Задача 2
a = ("1;2;3;100")
names = a.split(';')
names2 = []
names3 = []
for n in names:
    names2.append(int(n))
for k in names:
    names3.append(float(k))
print(names2)
print(names3)
#Задача 3
a = input('Введите номер телефона, записанный через дефис:')
parts = a.split('-')
result= ''.join(parts)
print(result)
#Задача 4
a = input('введите значение доходов хозяйства за месяц через запятую:')
b = a.split(',')
L = []
L2 = []
for n in b:
    L.append(int(n))
import math
for x in range(len(L)):
    L2.append(math.log(L[x]))
print(L2)
#Задача 5
words = ["Speak ", "to", "me ", "of", "Florence" ,"And ", "of", "the", "Renaissance"]
a = []
words_clean = []
for i in range(len(words)):
    a.append(words[i].lower())
for x in range(len(a)):
    words_clean.append(a[x].strip())
print(words_clean)

