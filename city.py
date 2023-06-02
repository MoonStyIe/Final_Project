# 도시 양극화 지수 탭

# 라이브러리
import streamlit as st
import json
import pandas as pd
import folium
from streamlit_folium import st_folium

def data_processing():
    # 데이터 불러오기
    geo_data = r'data/지수종합.geojson'
    with open(geo_data, encoding = 'utf-8') as f:
        geo_data = json.loads(f.read())
    data = pd.read_csv(r'data/지수종합_최종.csv',
                            encoding = 'cp949')
    return geo_data, data

# 사회, 경제, 양극화지수, 양극화 여부 folium 시각화 ## 지수페이지
def ES_folium_visual(geo_data, data, column):
    map = folium.Map(location=[36.6425, 127.489], zoom_start=9)

    folium.Choropleth(
        geo_data=geo_data,
        name="choropleth",
        data=data,
        columns=["행정구역", column],
        key_on='feature.properties.행정구역',
        fill_color="YlOrRd",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name=column,
    ).add_to(map)

    for i in range(len(data['행정구역'])):
        popup_content = ('행정구역 : ' + str(data['행정구역'][i]) + '<br>' +
                         '양극화 지수 : ' + str(data['양극화지수'][i]) + '<br>' +
                         '경제 지수 : ' + str(data['경제'][i]) + '<br>' +
                         '사회 지수 : ' + str(data['사회'][i]) + '<br>' +
                         '양극화 여부 : ' + str(data['target'][i]))
        popup = folium.Popup(popup_content, max_width=130)
        folium.Marker([data['latitude'][i], data['longitude'][i]],
                      popup=popup,
                      icon=folium.Icon(color='blue', icon='info-sign')).add_to(map)

    folium.LayerControl().add_to(map)

    st_folium(map, width=1000, height=600)

# ES_folium_visual(data, '양극화지수') # 사회, 경제, 양극화지수

# 소주제 folium 시각화
def folium_visual(geo_data, data, x, year):
    map = folium.Map(location = [36.6425, 127.489], zoom_start = 9)

    folium.Choropleth(
        geo_data = geo_data,
        name = "choropleth",
        data = data,
        columns = ["행정구역", x + '_' + str(year)],
        key_on = 'feature.properties.행정구역',
        fill_color = "YlOrRd",
        fill_opacity = 0.7,
        line_opacity = 0.2,
        legend_name = x,
    ).add_to(map)

    for i in range(len(data['행정구역'])):
        popup_content = ('행정구역 : ' + str(data['행정구역'][i]) + '<br>' +
                        f'{year}년 : ' + str(data[x + '_' + str(year)][i]))
        popup = folium.Popup(popup_content, max_width = 130)
        folium.Marker([data['latitude'][i], data['longitude'][i]],
                    popup = popup,
                    icon = folium.Icon(color = 'blue', icon = 'info-sign')).add_to(map)

    folium.LayerControl().add_to(map)

    return map

# folium_visual(data, 'grdp', 2015)

def run_city():
    geo_data, data = data_processing()
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

    with c4:
        st.markdown("- *10분위수를 구한 공식* \n", unsafe_allow_html = True)
        st.markdown("*설명란* \n", unsafe_allow_html = True)

    # 구분선
    st.write('<hr>', unsafe_allow_html=True)

    # 시각화
    ES_folium_visual(geo_data, data, '양극화지수')  # 사회, 경제, 양극화지수