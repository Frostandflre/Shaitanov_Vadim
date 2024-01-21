import pandas as pd
import openpyxl
df = pd.read_excel(
    io='ТАКСИ ЗАДАНИЕ 1.xlsx',
    engine='openpyxl',
    sheet_name='LOL',
    skiprows=0,
    usecols='A:D',
    nrows=16,
)

print(df)
