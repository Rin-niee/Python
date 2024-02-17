import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('C:\\Users\DNS\PycharmProjects\pythonProject1\Res-vyb.csv')
df.head()
df.info()
d = df[["kom1", "kom2", "kom3", "1", "2", "3", "4", "5", "6", "7", "8"]]  # выбор нужных столбцов
d.columns = ["region", "tk", "uk", "total", "invalid", "valid", "Pu", "Gru", "Jir", "Sob", "Yav"]  # присвоение названий
print(d.region.unique())  # выведение уникальных значений
d.groupby('region')  # группировка
for g in d.groupby('region'):  # группировка, занесение в кортеж
   g
print(d.groupby('region').agg('sum'))  # агрегирование по группам
print(d.groupby('region').agg('mean').head())  # подсчет и вывод среднего
print(d.groupby('region').agg(['mean', 'median']).head()) #вывод среднего и медианы
def my_diff(x): #разница между максимальными и минимальными значениями
   return max(x) - min(x)
print(d.groupby('region').agg(my_diff).head()) #использование функции внутри столбца
regs = d.groupby('region').agg('sum') #добавление столбца
regs["summast"] = regs.invalid + regs.valid #суммирование двух столбцов в новом
print(regs.head(3))
regs["summast_perc"] = regs.summast / regs.total * 100 #добавление столбца с явкой(в процентах)
print(regs.head(3))
def to_perc(x): #перевод в проценты
return x / regs.summast * 100
perc = regs[["Pu", "Gru", "Jir", "Sob", "Yav"]].apply(to_perc, axis = 0) #выбор и применение
print(perc.head(3))
old_cols = list(perc.columns) #переименование столбцов
new_cols = [x + "_perc" for x in old_cols]
perc.columns = new_cols
print(perc.head(3))
final = pd.concat([regs, perc], axis = 1) #соединение столбцов для показателей в одном месте
final.head()
final.plot.scatter('summast_perc', 'Gru_perc') #гистограмма
ax = final.plot.scatter('summast_perc', 'Gru_perc', color = "magenta") #задача цвета
ax.set_title('Scatterplot') #заголовок
ax.set_xlabel('summast rate (%)') #ось х
ax.set_ylabel('votes for Grudinin (%)') #ось у
plt.show()



