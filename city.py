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
        *GRDP는 한 지역의 국내총생산을 나타내는 지표입니다. 이는 해당 지역에서 생산된 상품과 서비스의 가치를 합한 값으로 경제적인 활동의 총량을 나타냅니다.
        GRDP는 지역 경제의 규모와 성장을 파악하고, 지역 간의 경제적 비교와 분석에 활용됩니다. 데이터를 시각화하여 GRDP의 추이와 산업별 패턴을 분석할 수 있습니다.*       
        \n""", unsafe_allow_html = True)

    # 해당하는 행정구역 선택
    area_select = st.sidebar.selectbox('⏏️ 목록', ['GRDP', '1인당 GRDP', '1인당 소비금액'])