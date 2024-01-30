import pandas as pd
import openpyxl
import streamlit as st
import plotly_express as px

st.set_page_config(page_title= "Шайтанов Вадим 2 задание",
                   page_icon=":monkey:",
                   layout="wide")
@st.cache
def get_data_from_excel():
    df = pd.read_excel(
        io='supermarkt_sales.xlsx',
        engine='openpyxl',
        sheet_name='Sales',
        skiprows=3,
        usecols='B:R',
        nrows=1000,
    )

    df["hour"] = pd.to_datetime(df["Time"],format="%H:%M:%S").dt.hour
    return df
df = get_data_from_excel()

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
df_selection =(df.iloc[219:420].query(
    'Branch == @Branch & City == @City & Customer_type == @Customer_type & Gender == @Gender & Product_line == @Product_line & Payment == @Payment'
))

st.title(':bar_chart: Ключевые показатели')
st.markdown('##')
total_sales = int(df_selection['Total'].sum())
average_rating = round(df_selection['Rating'].mean(),1)
star_rating = ':star:' * int(round(average_rating, 0))
average_sale_by_transaction = round(df_selection['Total'].mean(),2)
left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader('Итог:')
    st.subheader(f'US $ {total_sales:,}')
with middle_column:
    st.subheader('Средняя оценка')
    st.subheader(f'{average_rating }{star_rating}')
with right_column:
    st.subheader('Средняя скидка за транзакцию')
    st.subheader(f'US $ {average_sale_by_transaction:,}')

sales_by_product_line = (
    df_selection.groupby(by=["Product_line"]).sum()[["Total"]].sort_values(by="Total")
)
fig_product_sales = px.bar(
    sales_by_product_line,
    x="Total",
    y=sales_by_product_line.index,
    orientation="h",
    title="<b>Продажи</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    template="plotly_white",
)
fig_product_sales.update_layout(
    plot_bgcolor = "rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)
sales_by_hour = df_selection.groupby(by=["hour"]).sum()[["Total"]]
fig_hourly_sales = px.bar(
    sales_by_hour,
    x=sales_by_hour.index,
    y = "Total",
    title="<b>Продажи в час</b>",
    color_discrete_sequence=["#0083B8"]*len(sales_by_hour),
    template="plotly_white",
)
fig_hourly_sales.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor = "rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False))
)
left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_hourly_sales, use_container_width=True)
right_column.plotly_chart(fig_product_sales, use_container_width=True)
st.dataframe(df_selection)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style,unsafe_allow_html=True)