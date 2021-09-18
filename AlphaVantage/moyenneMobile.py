#programme sers à déterminer les moyennes mobiles sur un graphique pour connaitre les tendances
import pandas as pd
from alpha_vantage.timeseries import TimeSeries #retourne le prix en temps réel
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt

api_key = 'HC2BD89X3IXBW1YT'#la cle generee automatiquement

ts = TimeSeries(key = api_key, output_format='pandas')

data_ts, meta_data_ts = ts.get_intraday(symbol='MSFT', interval='1min', outputsize='full')#nous voulons toutes les données, toutes les minutes à partir du stock microsoft

period = 60 #une heure par periode

ti = TechIndicators(key=api_key, output_format='pandas')
#sma = simple moving average
data_ti, meta_data_ti = ti.get_sma(symbol='MSFT', interval='1min', time_period = period, series_type ='close')#close : moyenne mobile des prix fermés des stocks microsoft sur 60 periodes

df1 = data_ti
#data time series, avec la selection de la quatrieme colonne
df2 = data_ts['4. close'].iloc[period-1::]#iloc sers à selectionner les colonnes, on commence par la periode-1 (??) et on laisse les deux premieres colonnes

df2.index = df1.index #les index du deuxieme dataFrame est egal au premier
total_df=pd.concat([df1,df2], axis = 1)#la jointure des deux dataFrames sur l'axe qui est egal a 1
print(total_df)#retour avec la colonne date, colonne SMA(moyenne mobile simple) et la colonne des montants à la fermeture

total_df.plot()
plt.show()#affichage du graphique 