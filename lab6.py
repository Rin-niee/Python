#Задание 1
def identity(g):
    		return g*32
f = [12, 24, 36, 48, 109, 187]
b = list((map(identity, f)))
print(b)
 f = [12, 24, 36, 48, 109, 187]
b = list(map(lambda x: x*(25+7), f))
print(b)
#Задание 2
a = [9,1,4,7,3,5,5,3,2,1]
b = [9,1,4,9,6,9,7,8,3,5]
result = list(map(lambda x, y: x*y, a, b))
print(result)
#Задание 3
a = [9,1,4,7,3,5,5,3,2,1, 914, 735, 53, 21]
b = list(map(lambda x: x*25, a))
even = lambda y: y%2 ==0
c = list(filter(even, b))
onee = lambda y: y%2 !=0
d = list(filter(onee, b))
print(c, d)
#Задание 4
a = ['9','1','4','7','3','5','5','3','2','1']
b = []
for i in a:
    b.append(int(i))
c = list(map(lambda x: x//25, b))
d = list(map(lambda x: x/25, b))
f = list(map(lambda x: int(x), a))
#print(c)
#print(d)
print(f)

