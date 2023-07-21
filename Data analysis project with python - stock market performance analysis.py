#!/usr/bin/env python
# coding: utf-8

# In[116]:


pip install yfinance


# In[133]:


import pandas as pd
import yfinance as yf

start_date = '2020-01-01'
end_date = '2020-12-31'

tckrs = ['PEP','KO','MCD']

df_list_tickrs = []

for frame in tickers:
    data = yf.download(frame, start=start_date, end=end_date)
    df_list_tickrs.append(data)


# In[134]:


df = pd.concat(df_list_tickrs, keys = tickers, names = ['tickers','date'] )
df


# In[135]:


df = df.reset_index()
print(df.head())


# In[166]:


import plotly.express as px
pic = px.line(df, x='date', 
              y='Close', 
              color='tickers',
              labels= {'Close':'closing price', 'tickers':'company'},
              title="Stock Market Performance of pepsi, coca-cola and mcdonalds year - 2020")

pic.show()


# In[168]:


fctd= px.area(df, x='date', 
              y='Close', 
              facet_col='tickers', 
              labels= {'Close':'closing price', 'tickers':'company'},
              title="Stock Market Performance of pepsi, coca-cola and mcdonalds year - 2020")
fctd.update_traces(line_color='green')
fctd.show()


# In[182]:


pep = df.loc[df['tickers'] == 'PEP', ['date', 'Close']].rename(columns={'Close': 'PEP'})
ko = df.loc[df['tickers'] == 'KO', ['date', 'Close']].rename(columns={'Close': 'KO'})


# In[185]:


df_corr = pd.merge(pep, ko, on='date')

# create a scatter plot to visualize the correlation
pic = px.scatter(df_corr, x='PEP', y='KO', 
                 trendline='ols', 
                 title='Correlation between pepsi and coco-cola')
pic.show()


# In[190]:


mcd = df.loc[df['tickers'] == 'MCD', ['date', 'Close']].rename(columns={'Close': 'MCD'})
pep = df.loc[df['tickers'] == 'PEP', ['date', 'Close']].rename(columns={'Close': 'PEP'})


# In[191]:


df_corr = pd.merge(pep, mcd, on='date')

pic = px.scatter(df_corr, x='PEP', y='MCD', 
                 trendline='ols', 
                 title='Correlation between mcdonalds and pepsi')
pic.show()


# In[192]:


ko = df.loc[df['tickers'] == 'KO', ['date', 'Close']].rename(columns={'Close': 'KO-COCA COLA'})
mcd = df.loc[df['tickers'] == 'MCD', ['date', 'Close']].rename(columns={'Close': 'MCD-MCDONALDS'})


# In[194]:


df_corr = pd.merge(ko, mcd, on='date')

pic = px.scatter(df_corr, x='KO-COCA COLA', y='MCD-MCDONALDS', 
                 trendline='ols', 
                 title='Correlation between coca-cola and mcdonalds')
pic.show()


# In[ ]:




