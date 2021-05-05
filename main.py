import numpy as np
import pandas as pd
import xlrd
import openpyxl

#zadanie1

# xlsx = pd.ExcelFile('imiona.xlsx')
# data = pd.read_excel(xlsx,header=0)
# df = pd.DataFrame(data)

# print(df)

#zadanie2

# print(df[df['Liczba']<1000])

# gr = df.groupby(['Imie'])
# print(gr.get_group('WOJCIECH'))

# grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
# print(grupa)

# print(df[(df['Rok'] >= 2005) & (df['Rok'] <= 2010)].groupby(['Rok']).agg({'Liczba':['sum']}))

# m=df[(df['Rok'] == 2000)& (df['Plec']=='M')].groupby(['Rok']).agg({'Liczba':['sum']})
# print(m)



#zadanie3

# df = pd.read_csv('zamowienia.csv',header=0,sep=';')


# print(df['Sprzedawca'].unique())

# x = df.sort_values(by = ['Utarg'],ascending=False)
# print(x.head(5))

# print(df.groupby(['Sprzedawca']).agg({'Sprzedawca':['unique']}))

# print(df.groupby(['Kraj']).agg({'idZamowienia':['count']}))

# suma = df[(df['Data zamowienia'] >= '2004-01-01') & (df['Data zamowienia'] <= '2004-12-31')]['Utarg'].mean()
# print(suma)
#
# srednia = df[(df['Data zamowienia'] >= '2005-01-01') & (df['Data zamowienia'] <= '2005-12-31')
# & (df['Kraj']=='Polska')].groupby(['Kraj']).agg({'idZamowienia':['count']})
# print(srednia)
#
# suma.to_csv('zamówienia_2004.csv',header=0,index=False)
# srednia.to_csv('zamówienia_2005.csv',header=0,index=False)