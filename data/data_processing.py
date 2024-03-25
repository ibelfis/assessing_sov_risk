import pandas as pd

df = pd.read_csv('data/raw_data.csv')


country_list=["BEN","BFA"] #["BEN","BFA","CAN","CHE","DEU","HTI","MLI","NOR","SEN"]
indic_list=["PV.EST","GE.EST"] #["PV.EST","GE.EST","IQ.CPA.FINQ.XQ","IQ.CPA.DEBT.XQ"]

selected_countries = df.loc[df['Country Code'].isin(country_list)]
selected_countries_indicators = selected_countries.loc[selected_countries['Indicator Code'].isin(indic_list)]

selected_countries_indicators = selected_countries_indicators.drop(['Country Name','Indicator Name'], axis=1)

selected_countries_indicators = selected_countries_indicators.drop(selected_countries_indicators.columns[-1], axis=1)


df2 = pd.melt(selected_countries_indicators, id_vars=['Country Code',"Indicator Code"], var_name='Date', value_name="Value")

print(df2)
