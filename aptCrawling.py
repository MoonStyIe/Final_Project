# -*- coding:utf-8 -*-
import requests
import pandas as pd

# Google Cloud
from google.cloud import bigquery
import pandas_gbq # 구글 빅쿼리와 함께 사용할 수 있는 패키지, pandas 데이터프레임과 BigQuery 간의 데이터 이동 용이

# API Key Settings
from utils import credentials, SERVICE_KEY
client = bigquery.Client(credentials=credentials)

def aptCrawling(SERVICE_KEY):
    data = None
    for j in range(1,2):
        url = f'http://openapi.seoul.go.kr:8088/{SERVICE_KEY}/json/tbLnOpendataRtmsV/{1+((j-1)*1000)}/{j*1000}'
        print(url)
        req = requests.get(url)
        content = req.json() # HTTP 요청의 응답(Response)에서 JSON 형식의 데이터를 추출하는 코드
        con = content['tbLnOpendataRtmsV']['row']
        result = pd.DataFrame(con)
        data = pd.concat([data, result])
    data = data.reset_index(drop=True) # 이전 인덱스를 삭제하고 새로운 연속적인 정수 인덱스로 재설정
    data['DEAL_YMD'] = pd.to_datetime(data['DEAL_YMD'], format=("%Y%m%d"))

    return data

def save2BQ(data):
    table_name = "seoul.realestate"
    project_id = "humanbigquery01"

    # Save the DataFrame to BigQuery
    pandas_gbq.to_gbq(data,
                      table_name,
                      project_id = project_id, if_exists = 'replace') # 테이블이 이미 존재하는 경우 기존 테이블 대체

if __name__ == "__main__":
    data = aptCrawling(SERVICE_KEY)
    save2BQ(data)