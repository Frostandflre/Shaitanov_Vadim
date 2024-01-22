import pandas as pd
import openpyxl
import streamlit as st

st.set_page_config(page_title= "Шайтанов Вадим 2 задание",
                   page_icon=":monkey:",
                   layout="wide")
df = pd.read_excel(
    io='supermarkt_sales.xlsx',
    engine='openpyxl',
    sheet_name='Sales',
    skiprows=313,
    usecols='B:R',
    nrows=200,
)

st.dataframe(df)