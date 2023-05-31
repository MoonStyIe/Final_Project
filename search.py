# 조회 탭

# 라이브러리
import streamlit as st
import json
import pandas as pd
import geopandas as gpd
import warnings
import folium

def data_processing():
    # 데이터 불러오기
    geo_data = r'C:\Users\YONSAI\Desktop\Python_Studying\Mapboxgl_package\data\GRDP.geojson'
    with open(geo_data) as f:
        geo_data = json.loads(f.read())
    grdp_data = pd.read_csv(r'C:\Users\YONSAI\Desktop\Python_Studying\Mapboxgl_package\data\GRDP_최종.csv',
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

    map

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

    map

# 데이터프레임 시각화
def data_visual_all(data): # 전체 데이터 출력
    st.dataframe(data)

def data_visual_per(data, percentile): # 10분위수 데이터 출력
    data_local = data[data['10분위수'] == percentile]
    data_local = data_local[['행정구역', '2015', '2016', '2017', '2018', '2019', '10분위수']]
    st.dataframe(data_local)

def run_search():
    selected = option_menu(None, ["GRDP", "🔎 행정구역별 소득분포", "📁 데이터", "📊 EDA"],
                           icons=['🏠', '🔎', '📁', '📊'], default_index=0, orientation="horizontal",
                           styles={
                               "container": {"padding": "0!important", "background-color": "#cccccc"},
                               "nav-link": {"font-size": "15px", "text-align": "left", "margin": "0px",
                                            "--hover-color": "#eee"},
                               "nav-link-selected": {"background-color": "red"},
                           }
                           )
    if selected == 'GRDP':
        st.markdown('GRDP')
        st.markdown('설명') # 지표 설명

        # 데이터 불러오기
        data_processing()

        # 셀렉 박스 (전체, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

        # 화면을 2:1 비율로 분할
        col1, col2 = st.columns([2, 1])
        with col1:
            st.header("지도")
        if selectbox == '전체':
            data_folium_all(geo_data, grdp_data)
        elif selectbox == '1':
            data_folium_local(geo_data, grdp_data, 1)
        elif selectbox == '2':
            data_folium_local(geo_data, grdp_data, 2)
        elif selectbox == '3':
            data_folium_local(geo_data, grdp_data, 3)
        elif selectbox == '4':
            data_folium_local(geo_data, grdp_data, 4)
        elif selectbox == '5':
            data_folium_local(geo_data, grdp_data, 5)
        elif selectbox == '6':
            data_folium_local(geo_data, grdp_data, 6)
        elif selectbox == '7':
            data_folium_local(geo_data, grdp_data, 7)
        elif selectbox == '8':
            data_folium_local(geo_data, grdp_data, 8)
        elif selectbox == '9':
            data_folium_local(geo_data, grdp_data, 9)
        elif selectbox == '10':
            data_folium_local(geo_data, grdp_data, 10)

        with col2:
            st.header("행정구역 정보")
        if selectbox == '전체':
            data_visual_all(data)
        elif selectbox == '1':
            data_visual_per(data, 1)
        elif selectbox == '2':
            data_visual_per(data, 2)
        elif selectbox == '3':
            data_visual_per(data, 3)
        elif selectbox == '4':
            data_visual_per(data, 4)
        elif selectbox == '5':
            data_visual_per(data, 5)
        elif selectbox == '6':
            data_visual_per(data, 6)
        elif selectbox == '7':
            data_visual_per(data, 7)
        elif selectbox == '8':
            data_visual_per(data, 8)
        elif selectbox == '9':
            data_visual_per(data, 9)
        elif selectbox == '10':
            data_visual_per(data, 10)

    # 추가 선 차트
    st.markdown('설명')
    st.markdown('선차트')