import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Сайт для мат.моделирования", page_icon=":chicken:")
st.title("Графопостроитель")
st.subheader("дайте мне свой файл Excel")

uploaded_file = st.file_uploader("Выберите файл", type="xlsx")
if uploaded_file:
    df = pd.read_excel(uploaded_file, engine="openpyxl")
    st.dataframe(df)
    groupby_column = st.selectbox(
        "Что вы хотите проанализировать?",
        ("Ship Mode", "Segment", "Category", "Sub-Category"),
    )
    output_columns = ["Sales", "Profit"]
    df_grouped = df.groupby(by=[groupby_column], as_index=False)[output_columns].sum()
    st.dataframe(df_grouped)