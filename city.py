# 도시 양극화 지수 탭

# 라이브러리
import streamlit as st
import json
import pandas as pd
import folium
from streamlit_folium import st_folium

def data_coming():
    '''데이터 불러오는 함수'''
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
    '''folium 지도 시각화 함수'''
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
    *※ 왼쪽 목록에서 조회하고자 하는 연도와 지수를 선택해주세요 ※*
    # """)

    c3, c4 = st.columns([2, 1])

    # 해당하는 행정구역 선택
    year_select = st.sidebar.selectbox('⏏️ 연도', ['2018년', '2019년', '2020년', '2021년'])

    if year_select == '2018년':
        jisu_select = st.sidebar.selectbox('⏏️ 목록', ['사회 지수', '경제 지수', '양극화 지수', '양극화 여부'])

        if jisu_select == '사회 지수':
            with c3:
                folium_visual_title(data_2018, geo_data_2018, '사회', '사회 지수')
            with c4:
                st.markdown("<h4 style='font-size: 24px; color: #333333;'>✔️ 사회 지수에 대한 설명 </h4>\n", unsafe_allow_html=True)

                text = '''\n 공공시설의 인구 비율에서 전국의 평균과 시군의 격차를 이용하여 양극화 지수를 개발하였습니다. 인구비율의 격차가 클수록 전국 평균보다 낮다는 뜻으로 양극화지수가 높아짐을 의미합니다. \n
: 전국 = 100 기준'''
                st.text_area('　', value=text, height=200)

                st.markdown("""
                - 어린이집 및 유치원 서비스권역 내 영유아인구비율 \n
                - 초등학교 서비스권역 내 학령인구 비율 \n
                - 병원, 주차장, 도서관, 공공체육시설 서비스권역 내 인구 비율 \n
                """, unsafe_allow_html=True)

        elif jisu_select == '경제 지수':
            with c3:
                folium_visual_title(data_2018, geo_data_2018, '경제', '경제 지수')
            with c4:
                st.markdown("<h4 style='font-size: 24px; color: #333333;'>✔️ 경제 지수에 대한 설명 </h4>\n", unsafe_allow_html=True)

                text = '''\n 부동산과 소득과 소비 데이터에서 전국의 평균과 시군의 \n격차를 이용하여 양극화 지수를 개발하였습니다.\n(단, GRDP는 지역내총생산이므로 서울 =100 기준으로 설정)\n \n격차가 클수록 전국 평균보다 낮다는 뜻으로 양극화지수가 높아짐을 의미합니다.\n
: 전국 = 100 기준\n'''
                st.text_area('　', value=text, height=200)

                st.markdown("""
                \n <자산>
                \n - 주택보급률 \n
                \n - 노후주택비율 \n
                \n - 주택가격 격차 \n
                \n <소득과 소비> \n
                \n - 1인당 소비가격 격차 \n
                \n - GRDP 격차 \n
                \n""", unsafe_allow_html=True)

        elif jisu_select == '양극화 지수':
            with c3:
                folium_visual_title(data_2018, geo_data_2018, '양극화지수', '양극화 지수')
            with c4:
                st.markdown("<h4 style='font-size: 24px; color: #333333;'>✔️ 양극화 지수에 대한 설명 </h4>\n", unsafe_allow_html=True)
                text = '''\n: 사회영역과 경제영역을 산술평균하여 종합 지수를 산출하였습니다.\n
양극화 지수가 높을수록 전국의 기준보다 낮다는 뜻이며, \n양극화 지수가 낮을수록 전국의 기준보다 높다는 뜻입니다.\n
서로의 격차를 이용하여 충청권의 양극화 지수가 얼마나 값이 차이나는지 확인할 수 있습니다.\n'''
                st.text_area('　', value=text, height=200)

        elif jisu_select == '양극화 여부':
            with c3:
                folium_visual_title(data_2018, geo_data_2018, 'target', '양극화 여부')
            with c4:
                st.markdown("<h4 style='font-size: 24px; color: #333333;'>✔️ 양극화 여부에 대한 설명 </h4>\n", unsafe_allow_html=True)

                text = '''\n: 각 년도별 평균을 기준으로 평균보다 높은 값은 양극화라고 판단하였습니다.\n
양극화가 1인 경우 전국평균에 비해 공공시설의 인구비율이 높으며, 주택가격, 1인당 소비가격, GRDP의 값이 높다는 뜻입니다.\n
즉, 인구가 다른 시,군에 비해 많이 사는 도시입니다. 양극화가 0인 경우 전국 평균에 비해 공공시설의 인구비율이 낮으며, 주택가격, 1인당 소비가격, GRDP의 값이 낮다는 뜻입니다.\n
결과적으로 인구가 다른 시,군에 비해 적게 사는 도시입니다.\n'''
                st.text_area('　', value=text, height=200)

    elif year_select == '2019년':
        jisu_select = st.sidebar.selectbox('⏏️ 목록', ['사회 지수', '경제 지수', '양극화 지수', '양극화 여부'])

        if jisu_select == '사회 지수':
            with c3:
                folium_visual_title(data_2019, geo_data_2019, '사회', '사회 지수')
            with c4:
                st.markdown("<h4 style='font-size: 24px; color: #333333;'>✔️ 사회 지수에 대한 설명 </h4>\n",
                            unsafe_allow_html=True)

                text = '''\n 공공시설의 인구 비율에서 전국의 평균과 시군의 격차를 이용하여 양극화 지수를 개발하였습니다. 인구비율의 격차가 클수록 전국 평균보다 낮다는 뜻으로 양극화지수가 높아짐을 의미합니다. \n
: 전국 = 100 기준'''
                st.text_area('　', value=text, height=200)

                st.markdown("""
                                - 어린이집 및 유치원 서비스권역 내 영유아인구비율 \n
                                - 초등학교 서비스권역 내 학령인구 비율 \n
                                - 병원, 주차장, 도서관, 공공체육시설 서비스권역 내 인구 비율 \n
                                """, unsafe_allow_html=True)

        elif jisu_select == '경제 지수':
            with c3:
                folium_visual_title(data_2019, geo_data_2019, '경제', '경제 지수')
            with c4:
                st.markdown("<h4 style='font-size: 24px; color: #333333;'>✔️ 경제 지수에 대한 설명 </h4>\n",
                            unsafe_allow_html=True)

                text = '''\n 부동산과 소득과 소비 데이터에서 전국의 평균과 시군의 \n격차를 이용하여 양극화 지수를 개발하였습니다.\n(단, GRDP는 지역내총생산이므로 서울 =100 기준으로 설정)\n \n격차가 클수록 전국 평균보다 낮다는 뜻으로 양극화지수가 높아짐을 의미합니다.\n
: 전국 = 100 기준\n'''
                st.text_area('　', value=text, height=200)

                st.markdown("""
                                \n <자산>
                                \n - 주택보급률 \n
                                \n - 노후주택비율 \n
                                \n - 주택가격 격차 \n
                                \n <소득과 소비> \n
                                \n - 1인당 소비가격 격차 \n
                                \n - GRDP 격차 \n
                                \n""", unsafe_allow_html=True)

        elif jisu_select == '양극화 지수':
            with c3:
                folium_visual_title(data_2019, geo_data_2019, '양극화지수', '양극화 지수')
            with c4:
                st.markdown("<h4 style='font-size: 24px; color: #333333;'>✔️ 양극화 지수에 대한 설명 </h4>\n",
                            unsafe_allow_html=True)
                text = '''\n: 사회영역과 경제영역을 산술평균하여 종합 지수를 산출하였습니다.\n
양극화 지수가 높을수록 전국의 기준보다 낮다는 뜻이며, \n양극화 지수가 낮을수록 전국의 기준보다 높다는 뜻입니다.\n
서로의 격차를 이용하여 충청권의 양극화 지수가 얼마나 값이 차이나는지 확인할 수 있습니다.\n'''
                st.text_area('　', value=text, height=200)

        elif jisu_select == '양극화 여부':
            with c3:
                folium_visual_title(data_2019, geo_data_2019, 'target', '양극화 여부')
            with c4:
                st.markdown("<h4 style='font-size: 24px; color: #333333;'>✔️ 양극화 여부에 대한 설명 </h4>\n",
                            unsafe_allow_html=True)

                text = '''\n: 각 년도별 평균을 기준으로 평균보다 높은 값은 양극화라고 판단하였습니다.\n
양극화가 1인 경우 전국평균에 비해 공공시설의 인구비율이 높으며, 주택가격, 1인당 소비가격, GRDP의 값이 높다는 뜻입니다.\n
즉, 인구가 다른 시,군에 비해 많이 사는 도시입니다. 양극화가 0인 경우 전국 평균에 비해 공공시설의 인구비율이 낮으며, 주택가격, 1인당 소비가격, GRDP의 값이 낮다는 뜻입니다.\n
결과적으로 인구가 다른 시,군에 비해 적게 사는 도시입니다.\n'''
                st.text_area('　', value=text, height=200)

    elif year_select == '2020년':
        jisu_select = st.sidebar.selectbox('⏏️ 목록', ['사회 지수', '경제 지수', '양극화 지수', '양극화 여부'])

        if jisu_select == '사회 지수':
            with c3:
                folium_visual_title(data_2020, geo_data_2020, '사회', '사회 지수')
            with c4:
                st.markdown("<h4 style='font-size: 24px; color: #333333;'>✔️ 사회 지수에 대한 설명 </h4>\n",
                            unsafe_allow_html=True)

                text = '''\n 공공시설의 인구 비율에서 전국의 평균과 시군의 격차를 이용하여 양극화 지수를 개발하였습니다. 인구비율의 격차가 클수록 전국 평균보다 낮다는 뜻으로 양극화지수가 높아짐을 의미합니다. \n
: 전국 = 100 기준'''
                st.text_area('　', value=text, height=200)

                st.markdown("""
                                - 어린이집 및 유치원 서비스권역 내 영유아인구비율 \n
                                - 초등학교 서비스권역 내 학령인구 비율 \n
                                - 병원, 주차장, 도서관, 공공체육시설 서비스권역 내 인구 비율 \n
                                """, unsafe_allow_html=True)

        elif jisu_select == '경제 지수':
            with c3:
                folium_visual_title(data_2020, geo_data_2020, '경제', '경제 지수')
            with c4:
                st.markdown("<h4 style='font-size: 24px; color: #333333;'>✔️ 경제 지수에 대한 설명 </h4>\n",
                            unsafe_allow_html=True)

                text = '''\n 부동산과 소득과 소비 데이터에서 전국의 평균과 시군의 \n격차를 이용하여 양극화 지수를 개발하였습니다.\n(단, GRDP는 지역내총생산이므로 서울 =100 기준으로 설정)\n \n격차가 클수록 전국 평균보다 낮다는 뜻으로 양극화지수가 높아짐을 의미합니다.\n
: 전국 = 100 기준\n'''
                st.text_area('　', value=text, height=200)

                st.markdown("""
                                \n <자산>
                                \n - 주택보급률 \n
                                \n - 노후주택비율 \n
                                \n - 주택가격 격차 \n
                                \n <소득과 소비> \n
                                \n - 1인당 소비가격 격차 \n
                                \n - GRDP 격차 \n
                                \n""", unsafe_allow_html=True)

        elif jisu_select == '양극화 지수':
            with c3:
                folium_visual_title(data_2020, geo_data_2020, '양극화지수', '양극화 지수')
            with c4:
                st.markdown("<h4 style='font-size: 24px; color: #333333;'>✔️ 양극화 지수에 대한 설명 </h4>\n",
                            unsafe_allow_html=True)
                text = '''\n: 사회영역과 경제영역을 산술평균하여 종합 지수를 산출하였습니다.\n
양극화 지수가 높을수록 전국의 기준보다 낮다는 뜻이며, \n양극화 지수가 낮을수록 전국의 기준보다 높다는 뜻입니다.\n
서로의 격차를 이용하여 충청권의 양극화 지수가 얼마나 값이 차이나는지 확인할 수 있습니다.\n'''
                st.text_area('　', value=text, height=200)

        elif jisu_select == '양극화 여부':
            with c3:
                folium_visual_title(data_2020, geo_data_2020, 'target', '양극화 여부')
            with c4:
                st.markdown("<h4 style='font-size: 24px; color: #333333;'>✔️ 양극화 여부에 대한 설명 </h4>\n",
                            unsafe_allow_html=True)

                text = '''\n: 각 년도별 평균을 기준으로 평균보다 높은 값은 양극화라고 판단하였습니다.\n
양극화가 1인 경우 전국평균에 비해 공공시설의 인구비율이 높으며, 주택가격, 1인당 소비가격, GRDP의 값이 높다는 뜻입니다.\n
즉, 인구가 다른 시,군에 비해 많이 사는 도시입니다. 양극화가 0인 경우 전국 평균에 비해 공공시설의 인구비율이 낮으며, 주택가격, 1인당 소비가격, GRDP의 값이 낮다는 뜻입니다.\n
결과적으로 인구가 다른 시,군에 비해 적게 사는 도시입니다.\n'''
                st.text_area('　', value=text, height=200)

    elif year_select == '2021년':
        jisu_select = st.sidebar.selectbox('⏏️ 목록', ['사회 지수', '경제 지수', '양극화 지수', '양극화 여부'])

        if jisu_select == '사회 지수':
            with c3:
                folium_visual_title(data_2021, geo_data_2021, '사회', '사회 지수')
            with c4:
                st.markdown("<h4 style='font-size: 24px; color: #333333;'>✔️ 사회 지수에 대한 설명 </h4>\n",
                            unsafe_allow_html=True)

                text = '''\n 공공시설의 인구 비율에서 전국의 평균과 시군의 격차를 이용하여 양극화 지수를 개발하였습니다. 인구비율의 격차가 클수록 전국 평균보다 낮다는 뜻으로 양극화지수가 높아짐을 의미합니다. \n
: 전국 = 100 기준'''
                st.text_area('　', value=text, height=200)

                st.markdown("""
                                - 어린이집 및 유치원 서비스권역 내 영유아인구비율 \n
                                - 초등학교 서비스권역 내 학령인구 비율 \n
                                - 병원, 주차장, 도서관, 공공체육시설 서비스권역 내 인구 비율 \n
                                """, unsafe_allow_html=True)

        elif jisu_select == '경제 지수':
            with c3:
                folium_visual_title(data_2021, geo_data_2021, '경제', '경제 지수')
            with c4:
                st.markdown("<h4 style='font-size: 24px; color: #333333;'>✔️ 경제 지수에 대한 설명 </h4>\n",
                            unsafe_allow_html=True)

                text = '''\n 부동산과 소득과 소비 데이터에서 전국의 평균과 시군의 \n격차를 이용하여 양극화 지수를 개발하였습니다.\n(단, GRDP는 지역내총생산이므로 서울 =100 기준으로 설정)\n \n격차가 클수록 전국 평균보다 낮다는 뜻으로 양극화지수가 높아짐을 의미합니다.\n
: 전국 = 100 기준\n'''
                st.text_area('　', value=text, height=200)

                st.markdown("""
                                \n <자산>
                                \n - 주택보급률 \n
                                \n - 노후주택비율 \n
                                \n - 주택가격 격차 \n
                                \n <소득과 소비> \n
                                \n - 1인당 소비가격 격차 \n
                                \n - GRDP 격차 \n
                                \n""", unsafe_allow_html=True)

        elif jisu_select == '양극화 지수':
            with c3:
                folium_visual_title(data_2021, geo_data_2021, '양극화지수', '양극화 지수')
            with c4:
                st.markdown("<h4 style='font-size: 24px; color: #333333;'>✔️ 양극화 지수에 대한 설명 </h4>\n",
                            unsafe_allow_html=True)
                text = '''\n: 사회영역과 경제영역을 산술평균하여 종합 지수를 산출하였습니다.\n
양극화 지수가 높을수록 전국의 기준보다 낮다는 뜻이며, \n양극화 지수가 낮을수록 전국의 기준보다 높다는 뜻입니다.\n
서로의 격차를 이용하여 충청권의 양극화 지수가 얼마나 값이 차이나는지 확인할 수 있습니다.\n'''
                st.text_area('　', value=text, height=200)

        elif jisu_select == '양극화 여부':
            with c3:
                folium_visual_title(data_2021, geo_data_2021, 'target', '양극화 여부')
            with c4:
                st.markdown("<h4 style='font-size: 24px; color: #333333;'>✔️ 양극화 여부에 대한 설명 </h4>\n",
                            unsafe_allow_html=True)

                text = '''\n: 각 년도별 평균을 기준으로 평균보다 높은 값은 양극화라고 판단하였습니다.\n
양극화가 1인 경우 전국평균에 비해 공공시설의 인구비율이 높으며, 주택가격, 1인당 소비가격, GRDP의 값이 높다는 뜻입니다.\n
즉, 인구가 다른 시,군에 비해 많이 사는 도시입니다. 양극화가 0인 경우 전국 평균에 비해 공공시설의 인구비율이 낮으며, 주택가격, 1인당 소비가격, GRDP의 값이 낮다는 뜻입니다.\n
결과적으로 인구가 다른 시,군에 비해 적게 사는 도시입니다.\n'''
                st.text_area('　', value=text, height=200)
