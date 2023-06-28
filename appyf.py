import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px
from deep_translator import GoogleTranslator

#Titulo 
st.title('Indicadores Gráficos')

# colocando uma imagem no sidebar 
st.sidebar.image("image.png", use_column_width=True)

Ativo = st.sidebar.title('Escolha o Ativo')

#Algumas siglas de empresas encontradas no yfinance
ticker = st.sidebar.selectbox('ENBR3.SA',
		('ENBR3.SA','BBDC4.SA','BBAS3.SA','PETR4.SA','VALE5.SA','AALR3.SA','CMIG3.SA','CMIG4.SA','CNTO3.SA'))

# Escolhas de data de iníco e fim 
start_date = st.sidebar.date_input('Data Início', value = pd.to_datetime('2021-01-31', format='%Y-%m-%d'))
end_date = st.sidebar.date_input('Data Final')
tickerData = yf.Ticker(ticker)

Informa = st.sidebar.title('Sobre a Empresa')

# tradução com googletrans do texto a ser exibido sobre a empresa
Sobre = st.sidebar.write(GoogleTranslator(source='en', target='pt').translate(tickerData.info['longBusinessSummary']))

#Gráficos dos ativos como: fechamento ajustado, abertura, alta, e volume
data = yf.download(ticker, start=start_date, end=end_date, group_by='tickers')
fig = px.bar(data, x = data.index, y = data['Adj Close'], title = ticker)
st.plotly_chart(fig)
df = data
df[['Adj Close']]

data = yf.download(ticker, start=start_date, end=end_date)
fig = px.line(data, x = data.index, y = data['Open'], title = ticker)
st.plotly_chart(fig)
df[['Open']]

data = yf.download(ticker, start=start_date, end=end_date)
fig = px.line(data, x = data.index, y = data['High'], title = ticker)
st.plotly_chart(fig)
df[['High']]

data = yf.download(ticker, start=start_date, end=end_date)
fig = px.line(data, x = data.index, y = data['Volume'], title = ticker)
st.plotly_chart(fig)
df[['Volume']]

#para efeito de aprendizado: mudar imagem, pegar dados de uma planilha , mudar tipos de graficos.
