import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('C:\\Users\DNS\PycharmProjects\pythonProject1\Titanic.csv') #загрузка таблицы
df = pd.read_csv('C:\\Users\DNS\PycharmProjects\pythonProject1\Titanic.csv', index_col=0)#PassengerId индентификатор
df.head()
dfn=df.copy()
print(dfn)
dfn.dropna(axis=0, inplace = True) #удаление пустых элементов
dfn.info() #сводная информация
dfn.describe() #сводная статистическая информация
dfn['Age'].plot.hist(color = 'red') #гистограмма переменной Age
plt.title("Возраст")
plt.xlabel("Возраст пассажиров")
plt.ylabel("Проценты")
plt.show()
dfn.Fare.info() #описательные характеристики Стоимость билетов
d = list(dfn.columns) #названия столбцов в виде списка
d[1]='Class'#переименование столбца
dfn.columns = d
dfn.columns
female= dfn[dfn['Sex']=='female'] #фильтрация по женскому полу и сохранение в новой базе данных
print(female)
ymale = dfn[(dfn['Sex']=='male') & (dfn['Age'] < 32)] #фильтрация по мужскому полу, возрасту и создание новой базы данных
print(ymale)
classs = dfn[(dfn['Class']==1) | (dfn['Class'] ==2)] #фильтр пассажиров 1 и 2 класса
print(classs)
class2 = dfn[((dfn['Class']==1) | (dfn['Class'] ==2)) & (df['Survived'] ==1)] #фильтр выживших пассажиров 1 и 2 класса
print(class2)
dfn['Female'] = (dfn['Sex']) #Добавление столбца с значениями 0/1
dfn.head()
dfn.loc[(dfn['Female'] == 'male'), 'Female'] = 0
dfn.loc[(dfn['Female'] == 'female'), 'Female'] = 1
print(dfn)
def rename_cols(dfn):
 on = list(dfn.columns)
 nn = [i.lower() for i in on]
 dfn.columns = nn
 return dfn
dfn = rename_cols(dfn)
dfn.head()
print(dfn)
dfn.to_csv('Titanic-new.csv') #сохранение получившегося датафрейма в новый файл

