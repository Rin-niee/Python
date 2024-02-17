#Задание 1
rept = {"python" : " питон",
         "anaconda" : "анаконда",
         "tortoize" : " черепаха" }
rept["snake"]="змея"
rept["tortoise"]=rept.pop("tortoize")
for i in rept:
    print(rept[i],'по-английски будет', i)
#Задание 2
cnt = ["Andorra", "Belarus", "Denmark", "Kenya", "Jamaica", "Romania"]
fh = [1.0, 6.0, 1.0, 4.0, 2.5, 2.0]
c = dict(zip(cnt, fh))
print(c)
#Задание 2.1
cnt = ["Andorra", "Belarus", "Denmark", "Kenya", "Jamaica", "Romania"]
fh = [1.0, 6.0, 1.0, 4.0, 2.5, 2.0]
c = list(zip(cnt, fh))
dicttt = {x: y for x, y in c}
print(dicttt)
#Задание 3
pairs = [(2, 4), (4, 6), (0, 1), (5, 2), (9, 1), (3, 8)]
calc = {(x, y): x * y for x, y in pairs}
print(calc)
#Задание 4
grades = {'Anna': 4, 'Bob': 3, 'Claire': 5, 'Dick': 2, 'Elena': 5,
 'Fred': 5, 'George': 4, 'Kristina': 3, 'Nick': 2,
 'Ursula': 4, 'Viktor': 5}
excel = []
good = []
satisf = []
bad = []
for k in grades:
    print(k, grades[k])
    if grades[k] == 5:
        excel.append(k)
    elif grades[k] == 4:
        good.append(k)
    elif grades[k] == 3:
        satisf.append(k)
    else:
        bad.append(k)
print(k, grades[k])
print('excel:', excel)
print("good:", good)
print("satisf:", satisf)
print("bad:", bad)

