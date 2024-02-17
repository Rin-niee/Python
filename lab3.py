#Задача 1
a = int(input('Введите положительное число'))
if a > 0:
    print('Молодец!')
if a < 0:
    print('Это не положительное число.')
#Задача 2
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in a:
    if i >=8:
        print('Отлично')
    elif (i >= 6) and (i <8):
        print('Хорошо')
    elif (i >=4) and (i <6):
        print('Удовлетворительно')
    else:
        print('Плохо')
#Задача 3
a = ('fhek349UE')
b =input('Введите пароль')
if a == b:
    print('Login Success')
else: #a != b
    print('Incorrect password. try again!')
#Задача 4
a = [3, 7, 11, 23, 18, 48, 81]
c = int((input('Введите число')))
for i in range(len(a)):
    if c == a[i]:
        print('Мое любимое число!')
if c != a[i]:
    print('Эх, ну почему?')
#Задача 5
a = int(input('Введите целое число'))
if a %2 == 0:
    print('Это четное число')
else:
    print('Это нечетное число')
#Задача 6
a =str((input('Введите существительное')))
if a[0] == a[0].upper():
    print('Это имя собственное')
else: 
    print('Это имя нарицательное')
