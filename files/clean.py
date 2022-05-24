from audioop import avg
from cProfile import run
from itertools import count
import pandas as pd
import numpy as np 
import seaborn

def shapes(df1, df2):

    print('\n \n BD :  DF \n Shape: \n',df1.shape)
    print('\n Columns',df1.dtypes)
    print('\n \n BD : DF 150  \n Shape: \n',df2.shape)
    print(' \n Columns',df2.dtypes)

    
    df1 = df1.drop(columns=['taster_name','taster_twitter_handle'], axis= 0)

    wine_df = pd.concat([df1,df2], axis= 0)

    print('\n \n BD : WINES  \n Shape: \n',wine_df.shape)
    print(' \n Columns',wine_df.dtypes)

    return wine_df


def pricepoints(dataframe):

    dataframe['R price/points'] = dataframe.price/dataframe.points
    df_pricepoints = dataframe[['country', 'winery','variety','R price/points']]
    df_pricepoints = df_pricepoints.groupby('country')['R price/points'].agg(max)
    print('Precio calidad matriz \n', df_pricepoints)
    return(dataframe)

def resume(dataframe, category):

    cat = str(category)
    pointsdf = dataframe.groupby(cat)['points'].agg(max_points = 'max', min_points = 'min')
    pointsdf ['delta points'] = ((pointsdf.max_points - pointsdf.min_points))
    pricedf = dataframe.groupby(cat)['price'].agg(max_price = 'max', min_price = 'min')
    pricedf ['delta price'] = ((pricedf.max_price - pricedf.min_price))
    number_of_test = dataframe.groupby(cat)['description'].count()
    compacta = pd.concat([pointsdf,pricedf, number_of_test], axis = 1)
    compacta.fillna(0)
    print(compacta)


def run ():
    
    
    df = pd.read_csv(r'C:\Users\Usuario\Documents\Codes\wine_analysis\data\winemag-data-130k-v2.csv')
    df_150 = pd.read_csv(r'C:\Users\Usuario\Documents\Codes\wine_analysis\data\winemag-data_first150k.csv')

    wines = shapes(df,df_150)
    print('\n \n - - - - - - - - - - - - - - - -  - - - - - - - - - \n \n ')
    pricepoints(wines)
    categories = {'1': 'country', '2':'variety', '3': 'region_1'}
    

    for i in categories:
        print( '{} will be filter for {}'.format(i,categories[i]))


    selector = input('Please insert your seleccion: ')
    category = categories[selector]
    resume(wines,category)
    #print(wines.head(10))

    #analitycs(wines)

    #variety = wines['variety'].unique().tolist()
    #countries = wines['country'].unique().tolist()
    #region = wines['region_1'].unique().tolist()
    #wineries = wines['winery'].unique().tolist()

    #for i in variety:

    #    print(i)



if __name__ == '__main__':

    run()


