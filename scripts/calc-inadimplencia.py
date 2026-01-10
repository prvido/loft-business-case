#%%
import pandas as pd
import plotly.graph_objects as go
from glob import glob

files = glob('dados/inadimplência/*.csv')
df = pd.DataFrame()
for file in files:
    category = file.split('\\')[1].split('.csv')[0].replace('-', ' ').capitalize()
    temp = pd.read_csv(file, sep=';', decimal=',')
    temp.columns = ['Data', category]
    temp = temp.set_index('Data')
    df = pd.concat([df, temp], axis=1)
df = df.reset_index()

fig = go.Figure()

for col in df.columns:
    if col not in ['Data', 'Cartão de crédito']:
        fig.add_trace(go.Scatter(
            x = df['Data'],
            y = df[col],
            mode = 'lines+text',
            name = col,
            text=([None] * (len(df) - 1)) + [df[col].iloc[-1]],
            textposition='top right'
        ))


fig.update_layout(
    title='Série História de inadimplência em crédito flexível | BCB',
    margin=dict(l=60, r=40, t=80, b=110),
    annotations= [
        dict(
            text='Fonte: BCB 2025 | Elaborado por Pedro Romeiro Vido',
            xref='paper',
            yref='paper',
            x=0,
            y=-0.15,
            showarrow=False,
            align='left',
            font=dict(size=11, color='gray')
        )
    ]
)

fig.show()

# %%
