from matplotlib.pyplot import axes
import pandas as pd
import numpy as np 
import seaborn as sns
import statistics

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


def modules(dataframe,category):

    cat = str(category)
    categories = dataframe[cat].unique().tolist()
    for i in categories:

       print(i)


def pricepoints(dataframe,category):

    cat = str(category)
    dataframe['R price/points'] = dataframe.price/dataframe.points
    df_pricepoints = dataframe[['country', 'winery','region_1','variety','R price/points']]
    if cat =='variety':
        df_pricepoints = (df_pricepoints.groupby(by= cat)[['winery','R price/points']]).max()
    else:
        df_pricepoints = (df_pricepoints.groupby(by = cat)[['winery','R price/points']]).max()
    
    
    df_pricepoints = df_pricepoints.dropna(axis = 0, how='any')
    return(df_pricepoints)


def resume(dataframe, category):

    cat = str(category)
    pointsdf = dataframe.groupby(cat)['points'].agg(MxPts = 'max', MnPts = 'min',AVGPts = 'mean').round(1)
    pointsdf ['DTA Pts'] = ((pointsdf.MxPts - pointsdf.MnPts))
    pricedf = dataframe.groupby(cat)['price'].agg(MxPri = 'max', MnPri = 'min', AVGPri = 'mean').round(1)
    pricedf ['DTA price'] = ((pricedf.MxPri - pricedf.MnPri))
    number_of_test = dataframe.groupby(cat)['description'].count()
    compacta = pd.concat([pointsdf,pricedf, number_of_test], axis = 1)
    compacta.rename({'description': 'tested'}, axis=1, inplace=True)
    compacta.fillna(0)
    #mask = compacta['tested'] > statistics.mean(compacta['tested'])*0.01
    mask = compacta['tested'] > 50
    filtered = compacta[mask]
    return(filtered)




def run ():
    
    
    df = pd.read_csv(r'C:\Users\Usuario\Documents\Codes\wine_analysis\data\winemag-data-130k-v2.csv')
    df_150 = pd.read_csv(r'C:\Users\Usuario\Documents\Codes\wine_analysis\data\winemag-data_first150k.csv')

    wines = shapes(df,df_150)
    
    print('\n \n - - - - - - - - - - - - - - - -  - - - - - - - - - \n \n ')
    categories = {'1': 'country', '2':'variety', '3': 'region_1'}
    

    for i in categories:
        print( 'Insert {} if you want filter for {}'.format(i,categories[i]))
    selector = input('\n \n Please insert your seleccion: ')
    category = categories[selector]
    df_resume = resume(wines,category)
    print(df_resume)
    

    question_1 = input('\n \n Insert - y - if you want see price point resume ')
    if question_1 == 'y':

        df_qualityprice = pricepoints(wines,category)
        print(df_qualityprice)

    plots(wines)
    #analitycs(wines)





if __name__ == '__main__':

    run()


