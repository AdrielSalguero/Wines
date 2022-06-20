from re import I
import statistics
import matplotlib
import pandas as pd
import random
import seaborn as sns



dicc = {'1': 'Adriel', '2': 'Pablo' , '3': 'Juan Carlos'}

#ind = input('Please select your number : ')

#seleccion = dicc[ind]
#print(dicc)
#print(seleccion)



average = []

for i in range(20):

    average.append(random.randint(0,52))

#print(average)

promedio = statistics.mean(average)
#print(promedio)

dfaveg = pd.DataFrame(average, columns=['Numeros'])

dfavegs = dfaveg['Numeros']>statistics.mean(dfaveg['Numeros'])*0.2
filtered = dfaveg[dfavegs]
promedio = statistics.mean(filtered['Numeros'])
#print(promedio)
#print(filtered.shape)


l = [[1, 2, 3], [1, None, 4], [2, 1, 3], [1, 2, 2]]
df = pd.DataFrame(l, columns=["a", "b", "c"])
#print(df)
#print(df.groupby(by=["a"]).sum())
#print(df.groupby(by=["b"]).sum())
#print(df.groupby(by=["c"]).sum())

#df = pd.read_csv(r'C:\Users\Usuario\Documents\Codes\wine_analysis\data\winemag-data-130k-v2.csv')
#df_150 = pd.read_csv(r'C:\Users\Usuario\Documents\Codes\wine_analysis\data\winemag-data_first150k.csv')





#sns.histplot(data = df, x = "country", hue= "points")
#sns.scatterplot(data = df, x='points', y= 'price', hue = 'country')
#matplotlib.pyplot.show()



#print(df.dtypes)

lista =[]
#for i in df['price']:

#   if type(i) != float:
#       lista.append(i)

#print(lista)
titles = ['a','a','c','d','e']
positions = []
[positions.append((i+1)*2) for i in range(len(titles))]
print(positions)