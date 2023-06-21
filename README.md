# 충청권 도시 양극화 프로젝트 (2023.05.22 ~ 2023.06.14)
<br/>

## [1. Streamlit 웹 서비스](https://sukyungjang-final-project-app-j1pife.streamlit.app/ "Streamlit Link")<br/>

## [2. 발표 영상](https://www.youtube.com/watch?v=YZGgZdaFF78 "Presentation Link")<br/>

## [3. PDF 파일](https://github.com/SukyungJang/Store_Sales_Project/blob/main/pdf/Attention_final.pdf "PDF Link")<br/>

---

## 💡 목적

충청권 도시에 대해 소득 분포 별 공간 분석 및 지도 시각화, 충청권 도시 양극화 지수 개발, 이에 따른 웹 서비스 구현
<br/>

## 📁 데이터

균형발전지표: <https://www.nabis.go.kr/totalStatisticsDetailView.do?menucd=168> <br/>
충청권 e-지방지표: <https://kostat.go.kr/menu.es?mid=a70501000000> <br/>
NABIS 국가균형발전종합정보시스템: <https://www.nabis.go.kr/> <br/>
인스파일러 데이터 활용 포털: <https://insfiler.com/> <br/>
세종경영자문: <http://sjcounsel.com/> <br/>

## 📊 ERD

![image](https://github.com/SukyungJang/Final_Project/blob/main/img/ERD.png)

<br/>

## 🧑‍🤝‍🧑 팀 구성

- 사용언어 : Python 3.10.10
- 작업툴 : VS Code, pycharm
- 인원 : 3명
- 주요 업무 : 소득 분포 별 공간 분석 및 지도 시각화, 도시 양극화 지수 개발, 웹 서비스 구현
- 기간 : 2023.05.22 ~ 2023.06.14
<br/>

## 💻 주요 기능

- **개요**
  - 프로젝트 개요 설명

- **행정구역별 소득분포**
  - 충청권 지역별 GRDP, 1인당 GRDP, 1인당 소비금액 10분위 분배 및 지도 시각화

![image](https://github.com/SukyungJang/Final_Project/blob/main/img/GRDP.png)

  - 연도별 선 그래프

![image](https://github.com/SukyungJang/Final_Project/blob/main/img/GRDPLINE.png)

- **1차 도시 양극화 지수**
  - 충남형 도시 양극화 지수와 균형발전지표 활용 1차 도시 양극화 지수 개발을 활용한 지도 시각화

![image](https://github.com/SukyungJang/Final_Project/blob/main/img/1차양극화.png)

- **최종 도시 양극화 지수**
  - 1차 양극화 지수를 로지스틱 회귀분석을 통해 개발하여 최종 도시 양극화 지수 개발을 활용한 지도 시각화

![image](https://github.com/SukyungJang/Final_Project/blob/main/img/최종양극화.png)

## 📥 설치 방법

### Windows
- 버전 확인
  - VS Code : 
  - Python : 3.10.10
  - 라이브러리 : Json(0.9.14), Pandas(2.0.1), Folium(0.14.0), Plotly(5.14.1), Plotly_express(0.4.1), streamlit(1.22.0), scikit-learn(1.2.2), seaborn(0.12.2)

- 프로젝트 파일을 다운로드 받습니다.
```
git clone https://github.com/SukyungJang/Final_Project.git
```
- 프로젝트 경로에서 가상환경 설치 후 접속합니다. (Windows 10 기준)
```
virtualenv venv
source venv/Scripts/activate
```
- 라이브러리를 설치합니다.
```
pip install -r requirements.txt
```
- streamlit 명령어를 실행합니다.
```
streamlit run app.py
```
<br/>

## 📅 주요 기능 업데이트 내용 <br/>
*2023-05-22(월)*
- 대시보드
    + 홈 탭, 조회 탭, EDA 탭 작성
    + 홈 탭의 프로젝트 개요 작성
- PPT
    + 표지 작성
    + 목차 초안 작성

---

*2023-05-23(화)*
- 대시보드
    + 조회 탭의 도별 탭 작성
    + 조회 탭의 시별 탭 작성
    + 수원시 탭의 샘플 지도 작성
- PPT
    + 표지 재작업
    + 목차 완성
    + 상세 목차 작성
    + 프로젝트 개요 작성
    + 팀 역할분담 페이지 작성 및 임시 플롯 차트 완성
- 데이터 수집
    + 나비스(NABIS) 국가균형발전종합정보시스템 데이터 수집
    + 균형지표 관련 데이터 수집
    + 전국 위도·경도 데이터 수집

---

*2023-05-24(수)*
- PPT
    + 목차 재작업
- 데이터 수집
    + 균형발전지표 데이터 수집, 전처리
    + 나비스(NAVIS) 데이터 전처리

---

*2023-05-25(목)*
- 대시보드
    + 데이터 탭 작성
    + 조회 탭 재구성
- PPT
    + 목차 재정비
    + 연구배경 작성
    + 연구목적 작성
    + 선정배경 작성
- 데이터 수집
    + 빅쿼리(BigQuery) 데이터 적재
    + 충청도 데이터 수집
    + 충청지방통계청에서 충청도권 데이터 수집
    + 충남형 양극화 지수 현황판 확인을 위해 충청남도 데이터 담당자에게 전화로 문의
- QGIS
    + 지도구현
- 분석
    + 회귀분석 공부

---

*2023-05-26(금)*
- 대시보드
    + 조회 탭 재구성
- PPT
    + 목차 재구성
    + 양극화 설명 도식화
    + 충청도 선정 보충설명
- 데이터 수집
    + 빅쿼리(BigQuery) 샘플 데이터 적재
    + 수집한 데이터 통합 및 배포
- QGIS
    + 지도구현
- 분석
    + 지수 개발에 이용할 대영역 소영역 구분
    + 로지스틱 회귀분석 공부
- ERD
    + mapboxgl을 이용한 지도 시각화 연습
    + folium을 이용한 지도 시각화 연습
    + geopandas를 이용한 지도 시각화 연습

---

*2023-05-30(화)*
- 대시보드
    + home 탭 -> 소개 탭 재구성
    + 소개 탭 링크 작성
    + 조회 탭 -> 행정구역별 소득분포 탭 재구성
    + mapboxgl 라이브러리를 이용한 시각화 데이터 업로드 시도했으나, 기능 문제로 실패
- PPT
    + 목차 재구성
    + 임시 웹서비스 소개 탭 작성
    + 개발환경 탭 작성
    + 연구목적 탭 재구성
- 데이터 수집
    + 주택 가격 동향 데이터 수집
    + 점유형태별 데이터 수집
- QGIS
    + 인구 밀도 분석 테스트
- 분석
    + 점유형태별 데이터 정제
    + 복지사업 시군구별 수급권자 현황 데이터 정제
    + 양극화 변수 선택 및 데이터 전처리
- ERD
    + mapboxgl 라이브러리를 이용한 시각화 데이터
    + pydec 라이브러리를 이용한 시각화 데이터
    + folium 라이브러리를 이용한 시각화 데이터

---

2023-06-01(목)
- 대시보드
    + 행적구역별 소득분포 탭 완성
    + 도시 양극화 지수 탭 작성
- PPT
    + 목차 재작성
    + 웹서비스 소개 구조화
- 분석
    + 지수 개발
    + 로지스틱 회귀분석 검증
- ERD
    + folium을 이용해 행적구역별 소득분포 탭 시각화 작성
    + folium을 이용해 도시 양극화 지수 탭 시각화 작성

---

2023-06-02(금)
- 대시보드
    + 도시 양극화 지수 탭 재작성
- PPT
    + 모든 탭 재구성
- ERD
    + folium을 이용해 도시 양극화 지수 탭 시각화 작성

---

2023-06-05(월)
- PPT
    + 탭 재구성

---

2023-06-07(화)
- 대시보드
    + 도시 양극화 지수 시각화 추가
    + 도시 양극화 지수 설명 추가
- PPT
    + 개요 탭 재구성
    + 공간 분석 탭 재구성
- ERD
    + folium을 이용한 도시 양극화 지수 시각화

---
2023-06-08(수) ~ 
- PPT 정리