# 조회 탭

# 라이브러리
import streamlit as st
import json
import pandas as pd
import geopandas as gpd
import warnings
import streamlit_folium
import folium
from streamlit_option_menu import option_menu
from streamlit_folium import st_folium
import time

def data_processing():
    # 데이터 불러오기
    geo_data = r'C:\Users\YONSAI\Desktop\Final_Project\data\GRDP.geojson'
    with open(geo_data, encoding = 'utf-8') as f:
        geo_data = json.loads(f.read())
    grdp_data = pd.read_csv(r'C:\Users\YONSAI\Desktop\Final_Project\data\GRDP_최종.csv',
                            encoding = 'cp949')
    return geo_data, grdp_data
def data_folium_all(geo_data, data):
    map = folium.Map(location=[36.6425, 127.489], zoom_start=9)

    folium.Choropleth(
        geo_data = geo_data,
        name = "choropleth",
        data = data,
        columns = ["행정구역", "10분위수"],
        key_on = 'feature.properties.행정구역',
        fill_color = "YlOrRd",
        fill_opacity = 0.7,
        line_opacity = 0.2,
        legend_name = "GRDP 10분위수",
    ).add_to(map)

    for i in range(len(data['행정구역'])):
        popup_content = ('행정구역 : ' + str(data['행정구역'][i]) + '<br>' +
                         '2015년 : ' + str(data['2015'][i]) + '<br>' +
                         '2016년 : ' + str(data['2016'][i]) + '<br>' +
                         '2017년 : ' + str(data['2017'][i]) + '<br>' +
                         '2018년 : ' + str(data['2018'][i]) + '<br>' +
                         '2019년 : ' + str(data['2019'][i]) + '<br>' +
                         '10분위수 : ' + str(data['10분위수'][i]) + '분위수')
        popup = folium.Popup(popup_content, max_width = 130)
        folium.Marker([data['latitude'][i], data['longitude'][i]],
                      popup = popup,
                      icon = folium.Icon(color = 'blue', icon = 'info-sign')).add_to(map)

    folium.LayerControl().add_to(map)

    st_folium(map, width=1000, height=600)

def data_folium_local(geo_data, data, percentile):
    data_local = data[data['10분위수'] == percentile]

    map = folium.Map(location=[36.6425, 127.489], zoom_start=9) # 지도 생성

    folium.Choropleth(
        geo_data = geo_data,
        name = "choropleth",
        data = data_local,
        columns = ["행정구역", "10분위수"],
        key_on = 'feature.properties.행정구역',
        fill_color = "YlOrRd",
        fill_opacity = 0.7,
        line_opacity = 0.2,
        legend_name = "GRDP 10분위수",
    ).add_to(map)

    for i in range(len(data_local['행정구역'])):
        # 마커 내용
        popup_content = ('행정구역 : ' + str(data_local['행정구역'].values[i]) + '<br>' +
                         '2015년 : ' + str(data_local['2015'].values[i]) + '<br>' +
                         '2016년 : ' + str(data_local['2016'].values[i]) + '<br>' +
                         '2017년 : ' + str(data_local['2017'].values[i]) + '<br>' +
                         '2018년 : ' + str(data_local['2018'].values[i]) + '<br>' +
                         '2019년 : ' + str(data_local['2019'].values[i]) + '<br>' +
                         '10분위수 : ' + str(data_local['10분위수'].values[i]) + '분위수')
        popup = folium.Popup(popup_content, max_width = 130) # 마커 내용 두께 조절
        # 마커 생성
        folium.Marker([data_local['latitude'].values[i], data_local['longitude'].values[i]],
                      popup = popup,
                      icon = folium.Icon(color='blue', icon = 'info-sign')).add_to(map) # 마커 아이콘

    folium.LayerControl().add_to(map) # 상단 컬러바

    st_folium(map, width=1000, height=600)

# 데이터프레임 시각화
def data_visual_all(data): # 전체 데이터 출력
    st.dataframe(data, height = 600, width = 800)

def data_visual_per(data, percentile): # 10분위수 데이터 출력
    data_local = data[data['10분위수'] == percentile]
    data_local = data_local[['행정구역', '2015', '2016', '2017', '2018', '2019', '10분위수']]
    st.dataframe(data_local)

def run_search():
    # 데이터 불러오기
    geo_data, grdp_data = data_processing()

    st.markdown("""
    ### 🔎 행정구역별 소득분포 조회결과
    *※ 왼쪽 사이드바에서 확인하고자 하는 행정구역과 10분위수를 선택해주세요 ※*
    # """)

    # 해당하는 행정구역 선택
    area_select = st.sidebar.selectbox('⏏️ 행정구역', ['충청도', '세종특별시'])

    # 화면을 분할하고 첫 번재 컬럼의 너비를 두 번재 컬럼의 2배로 설정
    c1, c2 = st.columns([2, 1])
    if area_select == '충청도':
        grdp_select = st.sidebar.slider('10분위수', min_value = 0, max_value = 10, value = None, step=1)
        # button_clicked = st.sidebar.button('조회')
        # if button_clicked:
        #     with st.spinner('로딩중…'):
        if grdp_select == 0:
            with c1:
                st.markdown("##### 🗺️ 소득분포")
                data_folium_all(geo_data, grdp_data)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_all(grdp_data[['행정구역', '2015', '2016', '2017', '2018', '2019', '10분위수']])

        elif grdp_select == 1:
            with c1:
                st.markdown("##### 🗺️ 소득분포")
                data_folium_local(geo_data, grdp_data, 1)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per(grdp_data[['행정구역', '2015', '2016', '2017', '2018', '2019', '10분위수']], 1)

        elif grdp_select == 2:
            with c1:
                st.markdown("##### 🗺️ 소득분포")
                data_folium_local(geo_data, grdp_data, 2)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per(grdp_data[['행정구역', '2015', '2016', '2017', '2018', '2019', '10분위수']], 2)

        elif grdp_select == 3:
            with c1:
                st.markdown("##### 🗺️ 소득분포")
                data_folium_local(geo_data, grdp_data, 3)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per(grdp_data[['행정구역', '2015', '2016', '2017', '2018', '2019', '10분위수']], 3)

        elif grdp_select == 4:
            with c1:
                st.markdown("##### 🗺️ 소득분포")
                data_folium_local(geo_data, grdp_data, 4)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per(grdp_data[['행정구역', '2015', '2016', '2017', '2018', '2019', '10분위수']], 4)

        elif grdp_select == 5:
            with c1:
                st.markdown("##### 🗺️ 소득분포")
                data_folium_local(geo_data, grdp_data, 5)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per(grdp_data[['행정구역', '2015', '2016', '2017', '2018', '2019', '10분위수']], 5)

        elif grdp_select == 6:
            with c1:
                st.markdown("##### 🗺️ 소득분포")
                data_folium_local(geo_data, grdp_data, 6)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per(grdp_data[['행정구역', '2015', '2016', '2017', '2018', '2019', '10분위수']], 6)

        elif grdp_select == 7:
            with c1:
                st.markdown("##### 🗺️ 소득분포")
                data_folium_local(geo_data, grdp_data, 7)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per(grdp_data[['행정구역', '2015', '2016', '2017', '2018', '2019', '10분위수']], 7)

        elif grdp_select == 8:
            with c1:
                st.markdown("##### 🗺️ 소득분포")
                data_folium_local(geo_data, grdp_data, 8)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per(grdp_data[['행정구역', '2015', '2016', '2017', '2018', '2019', '10분위수']], 8)

        elif grdp_select == 9:
            with c1:
                st.markdown("##### 🗺️ 소득분포")
                data_folium_local(geo_data, grdp_data, 9)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per(grdp_data[['행정구역', '2015', '2016', '2017', '2018', '2019', '10분위수']], 9)

        elif grdp_select == 10:
            with c1:
                st.markdown("##### 🗺️ 소득분포")
                data_folium_local(geo_data, grdp_data, 10)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per(grdp_data[['행정구역', '2015', '2016', '2017', '2018', '2019', '10분위수']], 10)
