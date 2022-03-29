import pandas as pd
import numpy as np 
import seaborn



def main ():
    pass


df = pd.read_csv(r'C:\Users\Usuario\Documents\Codes\wine_analysis\data\winemag-data-130k-v2.csv')
df_150 = pd.read_csv(r'C:\Users\Usuario\Documents\Codes\wine_analysis\data\winemag-data_first150k.csv')
#dfj = pd.read_json(C:\Users\Usuario\Documents\Codes\wine_analysis\data\winemag-data-130k-v2.json)

print('\n \n BD :  DF \n Shape: \n',df.shape)
print('\n Columns',df.dtypes)
print('\n \n BD : DF 150  \n Shape: \n',df_150.shape)
print(' \n Columns',df_150.dtypes)

someliers = df
df = df.drop(columns=['taster_name','taster_twitter_handle'], axis= 0)

wine_df = pd.concat([df,df_150], axis= 0)

print('\n \n BD : WINES  \n Shape: \n',wine_df.shape)
print(' \n Columns',wine_df.dtypes)


