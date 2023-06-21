# 조회 탭

# 라이브러리
import streamlit as st
import json
import pandas as pd
import folium
from streamlit_folium import st_folium
import plotly_express as px

def data_processing():
    '''GRDP 데이터 불러오는 함수'''
    geo_data = r'data/GRDP.geojson'
    with open(geo_data, encoding = 'utf-8') as f:
        geo_data = json.loads(f.read())
    grdp_data = pd.read_csv(r'data/GRDP_최종.csv',
                            encoding = 'cp949')
    return geo_data, grdp_data

def data_processing2():
    '''1인당 GRDP 데이터 불러오는 함수'''
    geo_data = r'data/1인당_GRDP.geojson'
    with open(geo_data, encoding = 'utf-8') as f:
        geo_data = json.loads(f.read())
    grdp_data = pd.read_csv(r'data/1인당_GRDP_최종.csv',
                            encoding = 'cp949')
    return geo_data, grdp_data

def data_processing3():
    '''1인당 소비금액 데이터 불러오는 함수'''
    geo_data = r'data/1인당_소비금액.geojson'
    with open(geo_data, encoding = 'utf-8') as f:
        geo_data = json.loads(f.read())
    grdp_data = pd.read_csv(r'data/1인당_소비금액_최종.csv',
                            encoding = 'cp949')
    return geo_data, grdp_data

def data_folium_all(geo_data, data):
    '''folium 지도 시각화 함수'''
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
    '''folium 지역별 지도 시각화 함수'''
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
def data_visual_all_1(data):
    '''전체 데이터 출력 함수'''
    data = data[['행정구역', '2015', '2016', '2017', '2018', '2019', '10분위수']]
    st.dataframe(data, height = 600, width = 800)

def data_visual_all_2(data):
    '''전체 데이터 출력 함수'''
    data = data[['행정구역', '2018년', '2019년', '2020년', '10분위수']]
    st.dataframe(data, height = 600, width = 800)

def data_visual_all_3(data):
    '''전체 데이터 출력 함수'''
    data = data[['행정구역', '2018년', '2019년', '2020년', '10분위수']]
    st.dataframe(data, height = 600, width = 800)

def data_visual_per(data, percentile):
    '''10분위수 데이터 출력 함수'''
    data_local = data[data['10분위수'] == percentile]
    data_local = data_local[['행정구역', '2015', '2016', '2017', '2018', '2019', '10분위수']]
    st.dataframe(data_local)

def data_visual_per2(data, percentile):
    '''10분위수 데이터 출력 함수'''
    data_local = data[data['10분위수'] == percentile]
    data_local = data_local[['행정구역', '2018년', '2019년', '2020년', '10분위수']]
    st.dataframe(data_local)

def data_visual_per3(data, percentile):
    '''10분위수 데이터 출력 함수'''
    data_local = data[data['10분위수'] == percentile]
    data_local = data_local[['행정구역', '2018년', '2019년', '2020년', '10분위수']]
    st.dataframe(data_local)

# 선 차트
def grdp_line(grdp_data):
    '''GRDP 선 그래프 함수'''

    # 데이터프레임 생성
    grdp_data = pd.DataFrame(grdp_data)

    # 마크다운
    st.markdown("##### 📊 선 그래프")
    st.markdown("""
    *※ GRDP를 행정구역별로 나타낸 선 그래프 ※*
    # """)

    # 2015~2019년도의 값을 가지는 열들을 선택하여 데이터프레임 재구성
    df = pd.melt(grdp_data, id_vars = ['행정구역'], value_vars = ['2015', '2016', '2017', '2018', '2019'],
                var_name = '연도', value_name = 'GRDP')

    # 그래프 그리기
    fig = px.line(df, x = '연도', y = 'GRDP', color = '행정구역', line_group = '행정구역', hover_name = '행정구역',
                markers = True)

    # x축을 범주형으로 설정(x축이 연속형으로 설정되어 2,015.5 <- 이런식으로 나오는 것들을 없애기 위함)
    fig.update_layout(xaxis={'type': 'category'})

    st.plotly_chart(fig, use_container_width = 1000)

# 1인당_GRDP folium 시각화 함수
def grdp_one_all(geo_data, data):
    map = folium.Map(location=[36.6425, 127.489], zoom_start=9)
    folium.Choropleth(
        geo_data=geo_data,
        name="choropleth",
        data=data,
        columns=["행정구역", "10분위수"],
        key_on='feature.properties.행정구역',
        fill_color="YlOrRd",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="GRDP 10분위수",
    ).add_to(map)
    for i in range(len(data['행정구역'])):
        popup_content = ('행정구역 : ' + str(data['행정구역'][i]) + '<br>' +
                         '2018년 : ' + str(data['2018년'][i]) + '<br>' +
                         '2019년 : ' + str(data['2019년'][i]) + '<br>' +
                         '2020년 : ' + str(data['2020년'][i]) + '<br>' +
                         '10분위수 : ' + str(data['10분위수'][i]) + '분위수')
        popup = folium.Popup(popup_content, max_width=130)
        folium.Marker([data['latitude'][i], data['longitude'][i]],
                      popup=popup,
                      icon=folium.Icon(color='blue', icon='info-sign')).add_to(map)
    folium.LayerControl().add_to(map)

    st_folium(map, width=1000, height=600)

# 1인당_GRDP 10분위수별 folium 시각화 함수
def grdp_one_local(geo_data, data, percentile):
    '''1인당 GRDP 지도 시각화 함수'''
    grdp_local = data[data['10분위수'] == percentile]
    map = folium.Map(location = [36.6425, 127.489], zoom_start = 9)

    folium.Choropleth(
        geo_data = geo_data,
        name = "choropleth",
        data = grdp_local,
        columns = ["행정구역", "10분위수"],
        key_on = 'feature.properties.행정구역',
        fill_color = "YlOrRd",
        fill_opacity = 0.7,
        line_opacity = 0.2,
        legend_name = "GRDP 10분위수",
    ).add_to(map)

    for i in range(len(grdp_local['행정구역'])):
        popup_content = ('행정구역 : ' + str(grdp_local['행정구역'].values[i]) + '<br>' +
                        '2018년 : ' + str(grdp_local['2018년'].values[i]) + '<br>' +
                        '2019년 : ' + str(grdp_local['2019년'].values[i]) + '<br>' +
                        '2020년 : ' + str(grdp_local['2020년'].values[i]) + '<br>' +
                        '10분위수 : ' + str(grdp_local['10분위수'].values[i]) + '분위수')
        popup = folium.Popup(popup_content, max_width = 130)
        folium.Marker([grdp_local['latitude'].values[i], grdp_local['longitude'].values[i]],
                    popup = popup,
                    icon = folium.Icon(color = 'blue', icon = 'info-sign')).add_to(map)

    folium.LayerControl().add_to(map)

    st_folium(map, width=1000, height=600)


# 1인당 grdp 선 그래프
def grdp_one_line(data):
    '''1인당 GRDP 선 그래프 함수'''
    # 데이터프레임 생성
    data = pd.DataFrame(data)

    # 마크다운
    st.markdown("##### 📊 선 그래프")
    st.markdown("""
    *※ 1인당 GRDP를 행정구역별로 나타낸 선 그래프 ※*
    # """)

    # 2018 ~ 2020년도의 값을 가지는 열들을 선택하여 데이터프레임 재구성
    df = pd.melt(data, id_vars=['행정구역'], value_vars=['2018년', '2019년', '2020년'],
                 var_name='연도', value_name='GRDP')

    df = df.rename(columns={'GRDP': '1인당 GRDP'})

    df = pd.melt(data, id_vars=['행정구역'], value_vars=['2018년', '2019년', '2020년'],
                 var_name='연도', value_name='1인당 GRDP')

    # 그래프 그리기
    fig = px.line(df, x='연도', y='1인당 GRDP', color='행정구역', line_group='행정구역', hover_name='행정구역',
                  markers=True)

    st.plotly_chart(fig, use_container_width = 1000)

# 1인당 소비금액 folium 시각화
def cons_one_all(geo_data, data):
    '''1인당 소비금액 지도 시각화 함수'''
    map = folium.Map(location = [36.6425, 127.489], zoom_start = 9)

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
                        '2018년 : ' + str(data['2018년'][i]) + '<br>' +
                        '2019년 : ' + str(data['2019년'][i]) + '<br>' +
                        '2020년 : ' + str(data['2020년'][i]) + '<br>' +
                        '10분위수 : ' + str(data['10분위수'][i]) + '분위수')
        popup = folium.Popup(popup_content, max_width = 130)
        folium.Marker([data['latitude'][i], data['longitude'][i]],
                    popup = popup,
                    icon = folium.Icon(color = 'blue', icon = 'info-sign')).add_to(map)

    folium.LayerControl().add_to(map)

    st_folium(map, width=1000, height=600)

# 1인당 소비금액 지역별 folium 시각화
def cons_one_local(geo_data, data, percentile):
    '''1인당 소비금액 지도 시각화 함수'''
    grdp_local = data[data['10분위수'] == percentile]
    map = folium.Map(location = [36.6425, 127.489], zoom_start = 9)

    folium.Choropleth(
        geo_data = geo_data,
        name = "choropleth",
        data = grdp_local,
        columns = ["행정구역", "10분위수"],
        key_on = 'feature.properties.행정구역',
        fill_color = "YlOrRd",
        fill_opacity = 0.7,
        line_opacity = 0.2,
        legend_name = "GRDP 10분위수",
    ).add_to(map)

    for i in range(len(grdp_local['행정구역'])):
        popup_content = ('행정구역 : ' + str(grdp_local['행정구역'].values[i]) + '<br>' +
                        '2018년 : ' + str(grdp_local['2018년'].values[i]) + '<br>' +
                        '2019년 : ' + str(grdp_local['2019년'].values[i]) + '<br>' +
                        '2020년 : ' + str(grdp_local['2020년'].values[i]) + '<br>' +
                        '10분위수 : ' + str(grdp_local['10분위수'].values[i]) + '분위수')
        popup = folium.Popup(popup_content, max_width = 130)
        folium.Marker([grdp_local['latitude'].values[i], grdp_local['longitude'].values[i]],
                    popup = popup,
                    icon = folium.Icon(color = 'blue', icon = 'info-sign')).add_to(map)

    folium.LayerControl().add_to(map)

    st_folium(map, width=1000, height=600)

# 1인당 소비금액 선 그래프
def cons_one_line(data):
    '''1인당 소비금액 선 그래프 함수'''
    # 데이터프레임 생성
    data = pd.DataFrame(data)

    # 마크다운
    st.markdown("##### 📊 선 그래프")
    st.markdown("""
    *※ 1인당 소비금액을 행정구역별로 나타낸 선 그래프 ※*
    # """)

    # 2018~2020년도의 값을 가지는 열들을 선택하여 데이터프레임 재구성
    df = pd.melt(data, id_vars=['행정구역'], value_vars=['2018년', '2019년', '2020년'],
                 var_name='연도', value_name='GRDP')

    # 그래프 그리기
    fig = px.line(df, x='연도', y='GRDP', color='행정구역', line_group='행정구역', hover_name='행정구역',
                  markers=True)

    st.plotly_chart(fig, use_container_width=1000)

def cons_one_line_2(data):
    # 데이터프레임 생성
    data = pd.DataFrame(data)

    # 마크다운
    st.markdown("##### 📊 선 그래프")
    st.markdown("""
    *※ 1인당 소비금액을 행정구역별로 나타낸 선 그래프 ※*
    # """)

    # 2018~2020년도의 값을 가지는 열들을 선택하여 데이터프레임 재구성
    df = pd.melt(data, id_vars=['행정구역'], value_vars=['2018년', '2019년', '2020년'],
                 var_name='연도', value_name='GRDP')

    df = df.rename(columns={'GRDP': '1인당 소비금액'})

    df = pd.melt(data, id_vars=['행정구역'], value_vars=['2018년', '2019년', '2020년'],
                 var_name='연도', value_name='1인당 소비금액')

    # 그래프 그리기
    fig = px.line(df, x='연도', y='1인당 소비금액', color='행정구역', line_group='행정구역', hover_name='행정구역',
                  markers=True)

    st.plotly_chart(fig, use_container_width=1000)

def run_search():
    # 데이터 불러오기
    geo_data, grdp_data = data_processing()

    st.markdown("""
    ### 🔎 행정구역별 소득분포 조회결과
    *※ 왼쪽 목록에서 조회하고자 하는 데이터와 10분위수를 선택해주세요 ※*
    # """)

    # GRDP와 10분위수에 대한 설명
    c3, c4 = st.columns([2, 1])
    with c3:
        st.markdown("- *GRDP에 대한 설명* \n", unsafe_allow_html=True)
        st.markdown("""
        *GRDP는 한 지역의 국내총생산을 나타내는 지표입니다. 이는 해당 지역에서 생산된 상품과 서비스의 가치를 합한 값으로 경제적인 활동의 총량을 나타냅니다.
        GRDP는 지역 경제의 규모와 성장을 파악하고, 지역 간의 경제적 비교와 분석에 활용됩니다. 데이터를 시각화하여 GRDP의 추이와 산업별 패턴을 분석할 수 있습니다.*       
        \n""", unsafe_allow_html = True)

    with c4:
        st.markdown("- *10분위수를 구한 공식* \n", unsafe_allow_html = True)
        st.markdown("*최대값과 최소값을 10분위로 나누어 지역을 나눔* \n", unsafe_allow_html = True)

    # 구분선
    st.write('<hr>', unsafe_allow_html=True)

    # 해당하는 행정구역 선택
    area_select = st.sidebar.selectbox('⏏️ 목록', ['GRDP', '1인당 GRDP', '1인당 소비금액'])

    # 화면을 분할하고 첫 번재 컬럼의 너비를 두 번재 컬럼의 2배로 설정
    c1, c2 = st.columns([2, 1])
    if area_select == 'GRDP':
        grdp_select = st.sidebar.slider('10분위수', min_value = 0, max_value = 10, value = None, step=1)
        if grdp_select == 0:
            with c1:
                st.markdown("##### 🗺️ GRDP 소득분포")
                data_folium_all(geo_data, grdp_data)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_all_1(grdp_data)

        elif grdp_select == 1:
            with c1:
                st.markdown("##### 🗺️ GRDP 소득분포")
                data_folium_local(geo_data, grdp_data, 1)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per(grdp_data, 1)

        elif grdp_select == 2:
            with c1:
                st.markdown("##### 🗺️ GRDP 소득분포")
                data_folium_local(geo_data, grdp_data, 2)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per(grdp_data, 2)

        elif grdp_select == 3:
            with c1:
                st.markdown("##### 🗺️ GRDP 소득분포")
                data_folium_local(geo_data, grdp_data, 3)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per(grdp_data, 3)

        elif grdp_select == 4:
            with c1:
                st.markdown("##### 🗺️ GRDP 소득분포")
                data_folium_local(geo_data, grdp_data, 4)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per(grdp_data, 4)

        elif grdp_select == 5:
            with c1:
                st.markdown("##### 🗺️ GRDP 소득분포")
                data_folium_local(geo_data, grdp_data, 5)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per(grdp_data, 5)

        elif grdp_select == 6:
            with c1:
                st.markdown("##### 🗺️ GRDP 소득분포")
                data_folium_local(geo_data, grdp_data, 6)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per(grdp_data, 6)

        elif grdp_select == 7:
            with c1:
                st.markdown("##### 🗺️ GRDP 소득분포")
                data_folium_local(geo_data, grdp_data, 7)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per(grdp_data, 7)

        elif grdp_select == 8:
            with c1:
                st.markdown("##### 🗺️ GRDP 소득분포")
                data_folium_local(geo_data, grdp_data, 8)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per(grdp_data, 8)

        elif grdp_select == 9:
            with c1:
                st.markdown("##### 🗺️ GRDP 소득분포")
                data_folium_local(geo_data, grdp_data, 9)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per(grdp_data, 9)

        elif grdp_select == 10:
            with c1:
                st.markdown("##### 🗺️ GRDP 소득분포")
                data_folium_local(geo_data, grdp_data, 10)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per(grdp_data, 10)

        grdp_line(grdp_data)

    elif area_select == '1인당 GRDP':
        # 데이터 불러오기
        geo_data, grdp_data = data_processing2()

        # 화면을 분할하고 첫 번재 컬럼의 너비를 두 번재 컬럼의 2배로 설정
        c1, c2 = st.columns([2, 1])
        grdp_select2 = st.sidebar.slider('10분위수', min_value=0, max_value=10, value=None, step=1)
        if grdp_select2 == 0:
            with c1:
                st.markdown("##### 🗺️ 1인당 GRDP 소득분포")
                grdp_one_all(geo_data, grdp_data)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_all_2(grdp_data)

        elif grdp_select2 == 1:
            with c1:
                st.markdown("##### 🗺️ 1인당 GRDP 소득분포")
                grdp_one_local(geo_data, grdp_data, 1)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per2(grdp_data, 1)

        elif grdp_select2 == 2:
            with c1:
                st.markdown("##### 🗺️ 1인당 GRDP 소득분포")
                grdp_one_local(geo_data, grdp_data, 2)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per2(grdp_data, 2)

        elif grdp_select2 == 3:
            with c1:
                st.markdown("##### 🗺️ 1인당 GRDP 소득분포")
                grdp_one_local(geo_data, grdp_data, 3)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per2(grdp_data, 3)

        elif grdp_select2 == 4:
            with c1:
                st.markdown("##### 🗺️ 1인당 GRDP 소득분포")
                grdp_one_local(geo_data, grdp_data, 4)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per2(grdp_data, 4)

        elif grdp_select2 == 5:
            with c1:
                st.markdown("##### 🗺️ 1인당 GRDP 소득분포")
                grdp_one_local(geo_data, grdp_data, 5)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per2(grdp_data, 5)

        elif grdp_select2 == 6:
            with c1:
                st.markdown("##### 🗺️ 1인당 GRDP 소득분포")
                grdp_one_local(geo_data, grdp_data, 6)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per2(grdp_data, 6)

        elif grdp_select2 == 7:
            with c1:
                st.markdown("##### 🗺️ 1인당 GRDP 소득분포")
                grdp_one_local(geo_data, grdp_data, 7)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per2(grdp_data, 7)

        elif grdp_select2 == 8:
            with c1:
                st.markdown("##### 🗺️ 1인당 GRDP 소득분포")
                grdp_one_local(geo_data, grdp_data, 8)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per2(grdp_data, 8)

        elif grdp_select2 == 9:
            with c1:
                st.markdown("##### 🗺️ 1인당 GRDP 소득분포")
                grdp_one_local(geo_data, grdp_data, 9)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per2(grdp_data, 9)

        elif grdp_select2 == 10:
            with c1:
                st.markdown("##### 🗺️ 1인당 GRDP 소득분포")
                grdp_one_local(geo_data, grdp_data, 10)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per2(grdp_data, 10)

        grdp_one_line(grdp_data)

    elif area_select == '1인당 소비금액':
        # 데이터 불러오기
        geo_data, grdp_data = data_processing3()

        # 화면을 분할하고 첫 번재 컬럼의 너비를 두 번재 컬럼의 2배로 설정
        c1, c2 = st.columns([2, 1])
        grdp_select3 = st.sidebar.slider('10분위수', min_value=0, max_value=10, value=None, step=1)
        if grdp_select3 == 0:
            with c1:
                st.markdown("##### 🗺️ 1인당 소비금액")
                cons_one_all(geo_data, grdp_data)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_all_3(grdp_data)

        elif grdp_select3 == 1:
            with c1:
                st.markdown("##### 🗺️ 1인당 소비금액")
                cons_one_local(geo_data, grdp_data, 1)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per3(grdp_data, 1)

        elif grdp_select3 == 2:
            with c1:
                st.markdown("##### 🗺️ 1인당 소비금액")
                cons_one_local(geo_data, grdp_data, 2)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per3(grdp_data, 2)

        elif grdp_select3 == 3:
            with c1:
                st.markdown("##### 🗺️ 1인당 소비금액")
                cons_one_local(geo_data, grdp_data, 3)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per3(grdp_data, 3)

        elif grdp_select3 == 4:
            with c1:
                st.markdown("##### 🗺️ 1인당 소비금액")
                cons_one_local(geo_data, grdp_data, 4)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per3(grdp_data, 4)

        elif grdp_select3 == 5:
            with c1:
                st.markdown("##### 🗺️ 1인당 소비금액")
                cons_one_local(geo_data, grdp_data, 5)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per3(grdp_data, 5)

        elif grdp_select3 == 5:
            with c1:
                st.markdown("##### 🗺️ 1인당 소비금액")
                cons_one_local(geo_data, grdp_data, 5)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per3(grdp_data, 5)

        elif grdp_select3 == 6:
            with c1:
                st.markdown("##### 🗺️ 1인당 소비금액")
                cons_one_local(geo_data, grdp_data, 6)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per3(grdp_data, 6)

        elif grdp_select3 == 7:
            with c1:
                st.markdown("##### 🗺️ 1인당 소비금액")
                cons_one_local(geo_data, grdp_data, 7)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per3(grdp_data, 7)

        elif grdp_select3 == 8:
            with c1:
                st.markdown("##### 🗺️ 1인당 소비금액")
                cons_one_local(geo_data, grdp_data, 8)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per3(grdp_data, 8)

        elif grdp_select3 == 9:
            with c1:
                st.markdown("##### 🗺️ 1인당 소비금액")
                cons_one_local(geo_data, grdp_data, 9)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per3(grdp_data, 9)

        elif grdp_select3 == 10:
            with c1:
                st.markdown("##### 🗺️ 1인당 소비금액")
                cons_one_local(geo_data, grdp_data, 10)
            with c2:
                st.markdown("##### 📈 10분위수")
                data_visual_per3(grdp_data, 10)

        cons_one_line_2(grdp_data)