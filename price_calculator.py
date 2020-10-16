import pandas as pd

data = pd.read_csv(r'REVCO 2020 MAR (1).csv')

df = pd.DataFrame(data)


df['DPA plus 30 percent'] = (0.3 * df['DPA']) + df['DPA']

df['DPA plus 30 percent'] = df['DPA plus 30 percent'].round(2)

print(df['DPA plus 30 percent'])

df.to_csv(r'C:\Users\Kim\PycharmProjects\equipdirect_excel_pricer\Black_Stallion_revco_2020_with_equip_direct_pricing.csv')