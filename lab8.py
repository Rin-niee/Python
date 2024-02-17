import pandas as pd
df=pd.read_csv('C:\\Users\DNS\PycharmProjects\pythonProject1\9ussian_names.csv')
df.info() #вывод сводной информации
df.describe() #вывод статистической информации
df.columns #изменение названия столбцов
my_cols = list(df.columns)
my_cols[0] = "Number"
df.columns = my_cols
df.columns
df.drop(labels = [2], axis = 0) #удаление строк по индексу
df.drop(columns=['Name'],axis = 1, inplace = True) #удаление столбца
print(df)
