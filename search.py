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

def city():
    # prepare and read data
    shape = r'C:/Users/YONSAI/Desktop/Final_Project/data/Mapboxgl_package/data/siig.shp'
    data = gpd.read_file(shape, encoding = 'cp949')

    # 데이터프레임의 일부를 선택
    chungcheong = data.loc[135:164]
    daejeon = data.loc[64:68]
    sejong = data.loc[74:75]

    geometry = pd.concat([daejeon, sejong, chungcheong]).reset_index(drop = True)

    # 열 이름 변경을 위한 딕셔너리
    new_column_names = {'SIG_CD': '행정코드', 'SIG_ENG_NM': '행정영어', 'SIG_KOR_NM': '행정구역', 'geometry': 'geometry'}

    # 열 이름 변경 적용
    geometry = geometry.rename(columns=new_column_names)

    data = pd.read_csv(r'C:/Users/YONSAI/Desktop/Final_Project/data/Mapboxgl_package/data/1인당_GRDP.csv', encoding='cp949')

    # 데이터 합치기
    data = pd.merge(geometry, data, on='행정구역', how='outer')

    # 열 제거
    data.drop(columns=['행정코드', '행정영어'], axis=1, inplace=True)

    # 데이터 채우기
    data.iloc[6:10, 2:] = data.iloc[36, 2:]  # 청주시
    data.iloc[20:22, 2:] = data.iloc[37, 2:]  # 천안시

    # 행 제거
    data.drop(index=[36, 37], axis=0, inplace=True)

    # 10분위 수
    column_to_divide = '2020년'  # 분위를 계산할 열 선택

    percentiles = pd.qcut(data[column_to_divide], 10, labels=False)

    data['10분위수'] = percentiles + 1

    # GeoJSON으로 변환하여 저장합니다
    data.to_file(r'C:/Users/YONSAI/Desktop/Final_Project/data/Mapboxgl_package/data/1인당_GRDP.geojson', driver='GeoJSON')

    geo_data = r'C:/Users/YONSAI/Desktop/Final_Project/data/Mapboxgl_package/data/1인당_GRDP.geojson'
    with open(geo_data, encoding='utf-8') as f:
        geo_data = json.loads(f.read())

    # 토큰
    token = 'pk.eyJ1IjoibW9vbnN0eWxlIiwiYSI6ImNsaTQ2cnVlMzBobGczcXJiaXZmN3drcjcifQ.emASVayNBZqrif5WBVucKQ'

    # 청주시의 경도, 위도 입니다.
    center = [127.489, 36.6425]

    # 시각화 할 값에 따른 색상의 범주를 지정해줍니다.
    color_breaks = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    color_stops = create_color_stops(color_breaks, colors='YlOrBr')

    # ChoroplethViz 를 그립니다.
    viz = ChoroplethViz(
        access_token=token,
        data=geo_data,
        color_property='10분위수',
        color_stops=color_stops,
        center=center,
        line_color='black',
        line_width=3,
        line_opacity=1,
        opacity=1,
        zoom=8,
        below_layer='poi-label'
    )

    viz.show()
def run_search():
# 행정구역별 탭
    sidemenu = st.sidebar.selectbox('행정구역별', ['세종특별자치시', '대전광역시', '충청북도', '충청남도'])
    if sidemenu == '세종특별자치시':
        st.markdown("""
        *※ 조회결과입니다. ※*
        """)
        city()

# 대전관역시 구별 탭
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
