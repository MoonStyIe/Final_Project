import streamlit as st
from streamlit_option_menu import option_menu

# 도메인
st.set_page_config(page_title='도시 양극화 분석', page_icon='🌆')

# 홈
st.markdown("<h2 style='text-align: center; color: #333333;'>공간 빅데이터를 활용한 도시 양극화 분석</span></span>",unsafe_allow_html=True)
selected = option_menu(None, ["🏠 Home", "🔎 조회",  "📊 EDA"],
    icons = ['🏠', '🔎', '📊'],default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#cccccc"},
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "red"},
    }
)

# 홈 탭
if selected == "🏠 Home":
# 프로젝트 개요
    st.markdown("<h2 style='font-size: 24px; color: #333333;'>🔬 프로젝트 개요</h2>", unsafe_allow_html=True)
    st.write(
        """
*도시 양극화 문제의 사회적 관심이 늘어나고 있지만 뚜렷한 실태 파악이 어려움에 있으며 이를 해결하고자 지방자치단체, 민간 NGO 단체, 정부 기관 등에서 많은 심혈을 기울이고 있다.
개별경제 활동 인구에 금융 빅데이터와 공간정보 데이터를 융합하여 동태적인 도시 양극화 분석 단위와 분석 지표를 각각 마련하여 현 실태를 분석한 것을 목표로 하고자 한다.
공간분석 방법과 행위자 기반 모형을 개발하여 도시 양극화의 패턴을 찾아내고 영향요인을 파악한다.
또한 행위자 기반 모형적 접근으로 도시 양극과 추세를 파악하고 대응 시나리오 시뮬레이션을 개발하도록 한다.
그리고 분석의 결과로는 소득 분포 파악, 도시 양극화 공간적 패턴 파악, 도시 양극화 상태 지수 확인을 나타내도록 한다.*
        """
    )

# 구분선
    st.write('<hr>', unsafe_allow_html=True)

