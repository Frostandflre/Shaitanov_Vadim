import pandas as pd
import streamlit as st
import plotly.express as px
import base64
from io import StringIO,BytesIO

def generate_excel_download_link(df):
    # Credit Excel: https://discuss.streamlit.io/t/how-to-add-a-download-excel-csv-function-to-a-button/4474/5
    towrite = BytesIO()
    df.to_excel(towrite, index=False, header=True)  # write to BytesIO buffer
    towrite.seek(0)  # reset pointer
    b64 = base64.b64encode(towrite.read()).decode()
    href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="data_download.xlsx">Скачать таблицу</a>'
    return st.markdown(href, unsafe_allow_html=True)

def generate_html_download_link(fig):
    # Credit Plotly: https://discuss.streamlit.io/t/download-plotly-plot-as-html/4426/2
    towrite = StringIO()
    fig.write_html(towrite, include_plotlyjs="cdn")
    towrite = BytesIO(towrite.getvalue().encode())
    b64 = base64.b64encode(towrite.read()).decode()
    href = f'<a href="data:text/html;charset=utf-8;base64, {b64}" download="plot.html">Скачать график</a>'
    return st.markdown(href, unsafe_allow_html=True)


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

    fig = px.bar(
        df_grouped,
        x=groupby_column,
        y = "Sales",
        color="Profit",
        color_continuous_scale=["red", "yellow", "green"],
        template="plotly_white",
        title=f"<b>Продажи и прибыль согласно {groupby_column}</b>"
    )
    st.plotly_chart(fig)
    st.subheader("Загрузки")
    generate_excel_download_link(df_grouped)
    generate_html_download_link(fig)