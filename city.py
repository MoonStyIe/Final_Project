# 도시 양극화 지수 탭

# 라이브러리
import streamlit as st
import json
import pandas as pd
import folium
from streamlit_folium import st_folium

def data_coming():
    data_2018 = pd.read_csv(r'data/2018년.csv', encoding = 'cp949')
    geo_data_2018 = r'data/2018년.geojson'
    with open(geo_data_2018, encoding = 'utf-8') as f:
        geo_data_2018 = json.loads(f.read())

    data_2019 = pd.read_csv(r'data/2019년.csv', encoding = 'cp949')
    geo_data_2019 = r'data/2019년.geojson'
    with open(geo_data_2019, encoding = 'utf-8') as f:
        geo_data_2019 = json.loads(f.read())

    data_2020 = pd.read_csv(r'data/2020년.csv', encoding = 'cp949')
    geo_data_2020 = r'data/2020년.geojson'
    with open(geo_data_2020, encoding = 'utf-8') as f:
        geo_data_2020 = json.loads(f.read())

    data_2021 = pd.read_csv(r'data/2021년.csv', encoding = 'cp949')
    geo_data_2021 = r'data/2021년.geojson'
    with open(geo_data_2021, encoding = 'utf-8') as f:
        geo_data_2021 = json.loads(f.read())

    return data_2018, geo_data_2018, data_2019, geo_data_2019, data_2020, geo_data_2020, data_2021, geo_data_2021

# folium 시각화
def folium_visual_title(data, geo_data, col, kw):
    map = folium.Map(location = [36.6425, 127.489], zoom_start = 9)

    folium.Choropleth(
        geo_data = geo_data,
        name = "choropleth",
        data = data,
        columns = ["행정구역", col],
        key_on = 'feature.properties.행정구역',
        fill_color = "YlOrRd",
        fill_opacity = 0.7,
        line_opacity = 0.2,
        legend_name = col,
    ).add_to(map)

    for i in range(len(data['행정구역'])):
        popup_content = ('행정구역 : ' + str(data['행정구역'][i]) + '<br>' +
                        f'{kw} : ' + str(data[col][i]))
        popup = folium.Popup(popup_content, max_width = 130)
        folium.Marker([data['latitude'][i], data['longitude'][i]],
                    popup = popup,
                    icon = folium.Icon(color = 'blue', icon = 'info-sign')).add_to(map)

    folium.LayerControl().add_to(map)

    st_folium(map, width=1000, height=600)

def run_city():
    data_2018, geo_data_2018, data_2019, geo_data_2019, data_2020, geo_data_2020, data_2021, geo_data_2021 = data_coming()
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
    year_select = st.sidebar.selectbox('⏏️ 연도', ['2018년', '2019년', '2020년', '2021년'])

    if year_select == '2018년':
        jisu_select = st.sidebar.selectbox('⏏️ 목록', ['사회 지수', '경제 지수', '양극화 지수', '양극화 여부'])

        if jisu_select == '사회 지수':
            folium_visual_title(data_2018, geo_data_2018, '사회', '사회 지수')

        elif jisu_select == '경제 지수':
            folium_visual_title(data_2018, geo_data_2018, '경제', '경제 지수')

        elif jisu_select == '양극화 지수':
            folium_visual_title(data_2018, geo_data_2018, '양극화지수', '양극화 지수')

        elif jisu_select == '양극화 여부':
            folium_visual_title(data_2018, geo_data_2018, 'target', '양극화 여부')

    elif year_select == '2019년':
        jisu_select = st.sidebar.selectbox('⏏️ 목록', ['사회 지수', '경제 지수', '양극화 지수', '양극화 여부'])

        if jisu_select == '사회 지수':
            folium_visual_title(data_2019, geo_data_2019, '사회', '사회 지수')

        elif jisu_select == '경제 지수':
            folium_visual_title(data_2019, geo_data_2019, '경제', '경제 지수')

        elif jisu_select == '양극화 지수':
            folium_visual_title(data_2019, geo_data_2019, '양극화지수', '양극화 지수')

        elif jisu_select == '양극화 여부':
            folium_visual_title(data_2019, geo_data_2019, 'target', '양극화 여부')

    elif year_select == '2020년':
        jisu_select = st.sidebar.selectbox('⏏️ 목록', ['사회 지수', '경제 지수', '양극화 지수', '양극화 여부'])

        if jisu_select == '사회 지수':
            folium_visual_title(data_2020, geo_data_2020, '사회', '사회 지수')

        elif jisu_select == '경제 지수':
            folium_visual_title(data_2020, geo_data_2020, '경제', '경제 지수')

        elif jisu_select == '양극화 지수':
            folium_visual_title(data_2020, geo_data_2020, '양극화지수', '양극화 지수')

        elif jisu_select == '양극화 여부':
            folium_visual_title(data_2020, geo_data_2020, 'target', '양극화 여부')

    elif year_select == '2021년':
        jisu_select = st.sidebar.selectbox('⏏️ 목록', ['사회 지수', '경제 지수', '양극화 지수', '양극화 여부'])

        if jisu_select == '사회 지수':
            folium_visual_title(data_2021, geo_data_2021, '사회', '사회 지수')

        elif jisu_select == '경제 지수':
            folium_visual_title(data_2021, geo_data_2021, '경제', '경제 지수')

        elif jisu_select == '양극화 지수':
            folium_visual_title(data_2021, geo_data_2021, '양극화지수', '양극화 지수')

        elif jisu_select == '양극화 여부':
            folium_visual_title(data_2021, geo_data_2021, 'target', '양극화 여부')
