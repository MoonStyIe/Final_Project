# 조회 탭

# 라이브러리
import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image

def run_search():
# 도별 탭
    sidemenu = st.sidebar.selectbox('도별', ['경기도', '강원도', '경상북도', '경상남도', '전라북도', '전라남도', '충청북도', '충청남도'])
    if sidemenu == '경기도':
# 경기도 시별 탭
        submenu = st.sidebar.selectbox('시별', ['수원시', '성남시', '의정부시', '안양시', '부천시', '광명시', '평택시', '동두천시', '안산시', '고양시'])
        if submenu == '수원시':
            image_1 = Image.open('img/suwon.jpg')
            st.image(image_1)
# 강원도 시별 탭
    elif sidemenu == '강원도':
        submenu2 = st.sidebar.selectbox('시별', ['춘천시', '원주시', '강릉시', '동해시', '태백시', '속초시', '삼척시', '홍천시', '횡성시', '영월시'])