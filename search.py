# 조회 탭

# 라이브러리
import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image

def run_search():
# 행정구역별 탭
    sidemenu = st.sidebar.selectbox('행정구역별', ['세종특별시', '대전광역시', '충청북도', '충청남도'])
    if sidemenu == '세종특별시':
# 세종특별시 구별 탭
        submenu = st.sidebar.selectbox('구별', ['구이름을', '몰라요'])
        if submenu == '구이름을':
            st.markdown("""
            *※ 조회결과입니다. ※*
            """)
# 대전관역시 구별 탭
    elif sidemenu == '대전광역시':
        submenu2 = st.sidebar.selectbox('구별', ['구이름 하나도', '모릅니다.'])
        if submenu2 == '구이름 하나도':
            st.markdown("""
            *※ 조회결과입니다. ※*
            """)
# 충청북도 시별 탭
    elif sidemenu == '충청북도':
        submenu3 = st.sidebar.selectbox('시별', ['시1', '시2'])
        if submenu3 == '시1':
            st.markdown("""
            *※ 조회결과입니다. ※*
            """)
# 충청남도 시별 탭
    elif sidemenu == '충청남도':
        submenu4 = st.sidebar.selectbox('시별', ['시1', '시2'])
        if submenu4 == '시1':
            st.markdown("""
            *※ 조회결과입니다. ※*
            """)