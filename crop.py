import pandas as pd

pollution_data = pd.read_csv(r'bristol-air-quality-data.csv', sep=';')


pollution_data['Date Time'] = pd.to_datetime(pollution_data['Date Time'])

#look out for the cut-off date
find_date = "2010-01-01"

after_start_date = pollution_data['Date Time'] >= find_date
filtered_dates = pollution_data.loc[after_start_date]

#print(filtered_dates)
filtered_dates.to_csv('crop.csv', sep = ',', index=True)
