#%%
import pandas as pd
from glob import glob

df = pd.DataFrame()
for file in glob('../dados/saldo-crédito/*.csv'):
    category = file.split('\\')[1].split('.csv')[0].replace('-', ' ').capitalize()
    temp = pd.read_csv(file, sep=';', decimal=',')
    temp.columns = ['Data', category]
    temp = temp.set_index('Data')
    df = pd.concat([df, temp], axis=1)

df = df.reset_index()

df['Versátil'] = df['Cartão de crédito'] + df['Cheque especial']
df['Não versátil'] = df['Total'] - df['Versátil']

df['Peso versátil'] = df['Versátil'] / df['Total'] * 100
df['Peso não versátil'] = df['Não versátil'] / df['Total'] * 100

df
# %%
