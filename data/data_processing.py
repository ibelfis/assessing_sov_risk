import pandas as pd

df = pd.read_csv('data/raw_data.csv')

selected_countries = df.loc[df['Country Code'].isin(["BEN","BFA","CAN","CHE","DEU","HTI","MLI","NOR","SEN"])]

selected_countries_indicators = selected_countries.loc[selected_countries['Indicator Code'].isin(["PV.EST","GE.EST","IQ.CPA.FINQ.XQ","IQ.CPA.DEBT.XQ"])]

print(selected_countries_indicators.tail())
