import pandas as pd
import alpha_vantage
from alpha_vantage.timeseries import TimeSeries
import time
from openpyxl import load_workbook
import xlsxwriter#import va avec to_excel


api_key = 'HC2BD89X3IXBW1YT'#clé à récupérer sur le site de alphavantage

ts=TimeSeries(key=api_key, output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT', interval='1min', outputsize='full')#si on veut les dates minutes par minute
print(data)

#sauvegarde de données
i =1
#while i==1:
#    data, meta_data = ts.get_intraday(symbol='MSFT', interval='1min', outputsize='full')#si on veut les dates minutes par minute
#    data.to_excel('donneesMSFT.xlsx')#enregistrement dans un fichier excel
#    time.sleep(60)

#trouver de la volatilité 

close_data = data['4. close']#choix de la colonne 4
percentage_change = close_data.pct_change()#calcul de pourcentage d'écart entre les valeurs les plus proches entre elles

print(percentage_change)

last_change = percentage_change[-1]#analyse de la derniere colonne

if abs(last_change) > 0.0000:#si la valeur absolue de la derniere difference est au dessus d'une certaine valeur, alors on fait une action
	print("Alerte MSFT : " + str(last_change))

data.to_excel('donneesMSFT.xlsx')#enregistrement dans un fichier excel
data.to_csv('donneesMSFTCSV.csv')