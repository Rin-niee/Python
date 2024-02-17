#Задание 1
a = int(input('Введите число'))
def square(a):
   		 return a**2
print(square(a))
a = int(input('Введите число'))
def square(a):
    return a**2
print("Квадрат числа равен:")
square(a)
a = int(input('Введите число'))
def square(a):
 	return a**2
print("Квадрат числа равен:",square(a))
#Задание 2
a = int(input('Введите число'))
def nums(a):
    f = a - 1
    g = a+1
    return(list((f, g)))
print(nums(a))
#Задание 3
a = (input('Введите строку через пробел'))
def str_lower(a):
    b = a.lower()
    return(b.split())
print(str_lower(a))
#задание 4
import math
a = input('Введите числа через запятую и пробел')
a1 = a. split(', ')
b = []
for x in a1:
    b.append(float(x))
def my_log(b):
    c = []
    for i in range(len(b)):
        if b[i]>0:
            c.append(math.log(b[i]))
        else:
            c.append(None)
    return c
print(my_log(b))
#Задание 5
a = input('Введите имена людей через запятую')
b = input('Введите возраст людей через запятую')
a1 = a.split(',')
b1 = b.split(',')
def slovar(a1, b1):
    if len(a1) == len(b1):
        return(dict(zip(a1, b1)))
    else:
        return {}
if slovar(a1, b1) != {}:
    print(slovar(a1, b1))
else:
    print(("Списки имеют разную длину\n"),(slovar(a1, b1))) 
#Задание 6
p=float(input('Введите вероятность успеха'))
n=int(input('Введите количество попыток'))
k = int(input('Введите количество успехов'))
def factorial(n):
    f = 1
    for i in range(2, n+1):
        f = f*i
    return f
def binom(k, n):
    return factorial(n)//(factorial(k)*factorial(n-k))
def binom_prog(p,n,k):
    g = binom(k,n)*(p**k)*(1-p)**(n-k)
    return g
print(binom_prog(p,n,k))
#Задание 7
a =(input("введите значения через запятую"))
def all_sort(a):
    a1 = a.split(',')
    b = []
    for i in a1:
        b.append(float(i))
    b.sort()
    return b
print(all_sort(a))


