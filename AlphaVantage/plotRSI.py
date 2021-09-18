import pandas as pd
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt

api_key = 'HC2BD89X3IXBW1YT'

period = 60 #nombre de periodes qui seront utilisés pour calculer les indicateurs

ti = TechIndicators(key=api_key, output_format ='pandas')

data_ti, meta_data_ti = ti.get_rsi(symbol='MSFT', interval='1min', time_period=period, series_type='close') #get relative string index (rsi)
#rechercher la formule de calul de rsi, mais en bref, c'est pour savoir si une action est sur ou sous achetee

data_sma, meta_data_sma = ti.get_sma(symbol='MSFT', interval='1min', time_period=period, series_type='close')#sma = simple moving average

df1 = data_sma.iloc[1::]#premier dataFrame selectionnant a partir de la seconde colonne plus le reste de la série
df2 = data_ti

df1.index = df2.index

fig,ax1 = plt.subplots()
ax1.plot(df1, 'b-')#ffichage des donnees de la dataFrame 1 en sur l'axe ax1 en bleu
ax2 = ax1.twinx()#affiche les valeurs sur le meme axe (??)
ax2.plot(df2, 'r.') #affichage des valeurs de la seconde DataFrame en points rouges
plt.title("Graphe moyennes mobiles et RSI")#ecriture de l'intitule du titre
plt.show()#fonction affichant le graphe, affichage de la volatilite de ce qui est survendu ou sousvendu