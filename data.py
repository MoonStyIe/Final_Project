# 데이터 탭

# 라이브러리
import streamlit as st
from google.cloud import bigquery

def run_data():
    # 서비스 계정 키 JSON 파일의 경로
    key_path = '.streamlit/final-project-387801-f98385d67d2f.json'

    # BigQuery 클라이언트 생성
    client = bigquery.Client.from_service_account_json(key_path)

    # 쿼리 작성
    project_id = 'final-project-387801'
    dataset_id = 'final_project'
    table_id = 'chung'
    query = f"""
    SELECT *
    FROM `{project_id}.{dataset_id}.{table_id}`
    """

    # 쿼리 실행 및 결과를 데이터프레임으로 변환
    df = client.query(query).to_dataframe()

    # 데이터프레임 출력
    st.dataframe(df)

    # Streamlit 애플리케이션 실행
    if __name__ == '__main__':
        run_data()
