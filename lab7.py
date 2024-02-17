# Строки.
# Задание 30
a = float(input('Введите число'))
print('%.2f' % a)
#Задание 59
a =input('Введите произвольные буквы')
print(len(a))
# Списки.
# Задание 31
a =input('Введите произвольные элементы списка через пробел')
l1 = a.split(' ')
b = int(input('Введите начальное число диапазона'))
b = b-1
c = int(input("Введите конечное число диапазона"))
l2 = l1[b:c]        
print(len(l2))
#Задание 50
people = [{'имя': 'Артем', 'возраст': 19, 'пол': 'мужской'}, {'имя': 'Аня', 'возраст': 29, 'пол': 'женский'},{'имя': 'Данил', 'возраст': 5, 'пол': 'мужской'}]
print(sorted(people, key=lambda x: x['имя']))
print(sorted(people, key=lambda x: x['возраст']))
print(sorted(people, key=lambda x: x['пол']))
# Словари.
# Задание 28
dicttt = {'Фрукты':['яблоко', 'виноград','ананас'], 'Овощи':['помидор','морковь','свекла']}
f = {x: sorted(y) for x, y in dicttt.items()}
print(f)
#Задание 17
a = input('Введите ключи через пробел')
b = input('Введите значения через пробел')
a1= a.split(" ")
b1 = b.split(' ')
d = dict(zip(a1, b1))
print({v:k for k,v in {d[k]:k for k in reversed(list(d))}.items()})
# Кортежи.
# Задание 24
li = [1543,95,12554,532, 2345,4978789 (65)]
schet = 0
for i in li:
    if type(i) == tuple:
        break
    else:
        schet += 1
print(schet)
# Задание 3
a = input(('Введите числа для создания кортежа через запятую'))
a1 = int(input('введите порядковый номер числа, который Вы хотите вывести'))
b = a.split(',')
b1 = tuple(b)
print(b1[a1-1])
# Условные операторы.
# Задание 29
a = [3,3,4,5,4,3,3]
b = 'O'
for i in range(len(a)):
    if a[i]%3==0:
        print(b*2)
    elif a[i]%3==1:
        print('', b*2)
    else:
        print(' ', b)
#Задание 23
a = [3,2,2,2,2,2,3]
b = 'O'
for i in range(len(a)):
    if a[i]%3==0:
        print(b*3)
    else:
        print(b,b)
# Функции.
# Задание 18
x = int(input('Введите число'))
def sqrl(x):
    return x**2
print(sqrl(x))
#Задание 5
n = int(input('Введите число, факториал которого хотите получить'))
f = 1
for i in range(2, n+1):
 f = f * i
print(f)

