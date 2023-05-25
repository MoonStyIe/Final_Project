import streamlit as st
import pandas as pd

def loadcsv():
    df = pd.read_csv('data/균형발전지표.csv', encoding='CP949')

    st.title("CSV 데이터 불러오기")

    file_path = "균형발전지표.csv"

    st.write("불러온 파일 이름 :", file_path)

    st.write("불러온 데이터 :")
    st.dataframe(df)

    return df



