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
    skiprows=3,
    usecols='B:R',
    nrows=1000,
)

st.sidebar.header('Выберите фильтры')
Branch = st.sidebar.multiselect(
    "Отделение",
    options=df['Branch'].unique(),
    default=df['Branch'].unique(),
)
City = st.sidebar.multiselect(
    "Город",
    options=df['City'].unique(),
    default=df['City'].unique(),
)
Customer_type = st.sidebar.multiselect(
    "Тип клиента",
    options=df['Customer_type'].unique(),
    default=df['Customer_type'].unique(),
)
Gender = st.sidebar.multiselect(
    "Пол клиента",
    options=df['Gender'].unique(),
    default=df['Gender'].unique(),
)
Product_line = st.sidebar.multiselect(
    "Линия продукта",
    options=df['Product_line'].unique(),
    default=df['Product_line'].unique(),
)
Payment = st.sidebar.multiselect(
    "Оплата",
    options=df['Payment'].unique(),
    default=df['Payment'].unique(),
)
df_selection =df.iloc[219:420].query(
    'Branch == @Branch & City == @City & Customer_type == @Customer_type & Gender == @Gender & Product_line == @Product_line & Payment == @Payment'
)
st.dataframe(df_selection)