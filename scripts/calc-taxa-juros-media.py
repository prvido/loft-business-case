# %%
import pandas as pd
from glob import glob

files = glob('dados/taxas-de-juros/*.csv')

df = pd.concat([
    pd.read_csv(file, sep=';', decimal=',')
    for file in files
])

df = df.groupby('Modalidade').agg({'TaxaJurosAoMes': ['mean', 'std'], 'TaxaJurosAoAno': ['mean', 'std']})
df = df.stack(level=0, future_stack=True)
df['cv'] = df['std'] / df['mean']

print('\nTaxas de crédito das modalidades versáteis em Dez de 2025')
print(df.to_markdown())
print('fonte: Banco Central, 2025 | Consolidado por Pedro Romeiro Vido\n')