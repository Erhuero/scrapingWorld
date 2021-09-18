import pandas as pd



excel_file="donneesMSFTCSV.csv"

df = pd.read_csv(excel_file)#lecture du fichier csv et conversion en data frame
#print(df.columns)
#print(df.head(5))

new_df = df.loc[:, "date":"2. high"]
#print(new_df)

simple_moving_average = new_df.rolling(window=7, on='date').mean()#moyenne des sept premieres lignes
print(simple_moving_average)