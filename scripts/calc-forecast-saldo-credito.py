# %%
import pandas as pd
from prophet import Prophet

df = pd.read_csv('../dados/saldo-crédito/total.csv', sep=';', decimal=',')




df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
df['ano'] = df['data'].dt.year
df = df.drop_duplicates(subset='ano', keep='last')

df['ds'] = df['data']
df['y'] = df['valor']

df = df[["ds", "y"]]

# Modelo simples
m = Prophet(
    yearly_seasonality=False,  # para série anual geralmente não faz sentido
    weekly_seasonality=False,
    daily_seasonality=False
)

m.fit(df)

future = m.make_future_dataframe(periods=5, freq="YS")  # Year Start
forecast = m.predict(future)

out = forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail(5)
out['yhat'].iloc[-1]
# %%
