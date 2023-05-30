
# 조회 탭

# 라이브러리
import streamlit as st
import mapboxgl
from mapboxgl.viz import *
import json
import pandas as pd
import geopandas as gpd
from mapboxgl.utils import df_to_geojson
from mapboxgl.utils import create_color_stops
import warnings
import geopandas as gpd
import json
import pydeck as pdk
from streamlit_folium import folium_static
import folium

def run_search():
# 행정구역별 탭
    sidemenu = st.sidebar.selectbox('행정구역별', ['세종특별자치시', '대전광역시', '충청북도', '충청남도'])
    if sidemenu == '세종특별자치시':
        st.markdown("""
        *※ 조회결과입니다. ※*
        """)

# 대전광역시 구별 탭
    elif sidemenu == '대전광역시':
        submenu2 = st.sidebar.selectbox('구별', ['대전광역시', '동구', '중구', '서구', '유성구', '대덕구'])
        if submenu2 == '대전광역시':
            st.markdown("""
            *※ 조회결과입니다. ※*
            """)

        elif submenu2 == '동구':
            st.markdown("""
            *※ 조회결과입니다. ※*
            """)

        elif submenu2 == '중구':
            st.markdown("""
            *※ 조회결과입니다. ※*
            """)

        elif submenu2 == '서구':
            st.markdown("""
            *※ 조회결과입니다. ※*
            """)

        elif submenu2 == '유성구':
            st.markdown("""
            *※ 조회결과입니다. ※*
            """)

        elif submenu2 == '대덕구':
            st.markdown("""
            *※ 조회결과입니다. ※*
            """)

# 충청북도 시별 탭
    elif sidemenu == '충청북도':
        submenu3 = st.sidebar.selectbox('시군별', ['충청북도', '충주시', '제천시', '청주시', '보은군', '옥천군', '영동군', '진천군', '괴산군', '음성군', '단양군', '증평군'])
        if submenu3 == '충청북도':
            st.markdown("""
            *※ 조회결과입니다. ※*
            """)

        elif submenu3 == '충주시':
            st.markdown("""
            *※ 조회결과입니다. ※*
            """)

        elif submenu3 == '제천시':
            st.markdown("""
            *※ 조회결과입니다. ※*
            """)

        elif submenu3 == '청주시':
            st.markdown("""
            *※ 조회결과입니다. ※*
            """)

        elif submenu3 == '보은군':
            st.markdown("""
            *※ 조회결과입니다. ※*
            """)

        elif submenu3 == '옥천군':
            st.markdown("""
            *※ 조회결과입니다. ※*
            """)

        elif submenu3 == '영동군':
            st.markdown("""
            *※ 조회결과입니다. ※*
            """)

        elif submenu3 == '진천군':
            st.markdown("""
            *※ 조회결과입니다. ※*
            """)

        elif submenu3 == '괴산군':
            st.markdown("""
            *※ 조회결과입니다. ※*
            """)

        elif submenu3 == '음성군':
            st.markdown("""
            *※ 조회결과입니다. ※*
            """)

        elif submenu3 == '단양군':
            st.markdown("""
            *※ 조회결과입니다. ※*
            """)

        elif submenu3 == '증평군':
            st.markdown("""
            *※ 조회결과입니다. ※*
            """)

# 충청남도 시별 탭
    elif sidemenu == '충청남도':
        submenu4 = st.sidebar.selectbox('시군별', ['충청남도', '천안시', '공주시', '보령시', '아산시', '서산시', '논산시', '계룡시', '당진시', '금산군', '부여군', '서천군', '청양군', '홍성군', '예산군', '태안군'])
        if submenu4 == '충청남도':
            st.markdown("""
            *※ 조회결과입니다. ※*
            """)

        elif submenu4 == '천안시':
            st.markdown("""
            *※ 조회결과입니다. ※*
            """)

        elif submenu4 == '공주시':
            st.markdown("""
            *※ 조회결과입니다. ※*
            """)

        elif submenu4 == '보령시':
            st.markdown("""
            *※ 조회결과입니다. ※*
            """)

        elif submenu4 == '아산시':
            st.markdown("""
            *※ 조회결과입니다. ※*
            """)

        elif submenu4 == '서산시':
            st.markdown("""
            *※ 조회결과입니다. ※*
            """)

        elif submenu4 == '논산시':
            st.markdown("""
            *※ 조회결과입니다. ※*
            """)

        elif submenu4 == '계룡시':
            st.markdown("""
            *※ 조회결과입니다. ※*
            """)

        elif submenu4 == '당진시':
            st.markdown("""
            *※ 조회결과입니다. ※*
            """)

        elif submenu4 == '금산군':
            st.markdown("""
            *※ 조회결과입니다. ※*
            """)

        elif submenu4 == '부여군':
            st.markdown("""
            *※ 조회결과입니다. ※*
            """)

        elif submenu4 == '서천군':
            st.markdown("""
            *※ 조회결과입니다. ※*
            """)

        elif submenu4 == '청양군':
            st.markdown("""
                *※ 조회결과입니다. ※*
                """)

        elif submenu4 == '홍성군':
            st.markdown("""
                *※ 조회결과입니다. ※*
                """)

        elif submenu4 == '예산군':
            st.markdown("""
                *※ 조회결과입니다. ※*
                """)

        elif submenu4 == '태안군':
            st.markdown("""
                *※ 조회결과입니다. ※*
                """)
