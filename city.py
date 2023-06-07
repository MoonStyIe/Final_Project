# 도시 양극화 지수 탭

# 라이브러리
import streamlit as st
import json
import pandas as pd
import folium
from streamlit_folium import st_folium

def run_city():
    st.markdown("""
    ### 🔎 도시 양극화 지수에 따른 지도시각화 조회결과
    *※ 왼쪽 목록에서 조회하고자 하는 데이터와 10분위수를 선택해주세요 ※*
    # """)

    # GRDP와 10분위수에 대한 설명
    c3, c4 = st.columns([2, 1])
    with c3:
        st.markdown("- *양극화 지수에 대한 설명* \n", unsafe_allow_html=True)
        st.markdown("""
        *도시 양극화 지수는 도시 내에서 경제, 사회, 인구 등의 요소에 대한 격차와 차별을 측정하는 지표입니다.
        도시 양극화는 경제적, 사회적으로 부유한 지역과 빈곤한 지역 간의 격차가 큰 상태를 의미합니다.*       
        \n""", unsafe_allow_html = True)

    # 해당하는 행정구역 선택
    area_select = st.sidebar.selectbox('⏏️ 목록', ['GRDP', '1인당 GRDP', '1인당 소비금액'])