import os
from dotenv import load_dotenv
from supabase import create_client, Client

#.env 파일 불러오기
load_dotenv()

#환경변수 세팅
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key)  #Type Hinting; 정적으로 Type 지정하는 방법

#[DB] articles 테이블 insert; auto로 지정해둔 것을 별도로 불러오지 않음
def insert_into__articles(article):
    response = (
        supabase.table('articles').insert({
            "title": article["title"],
            "link": article["link"]
        }).execute()
    )

    inserted_row = response.data[0]
    generated_uuid = inserted_row['id']

    return generated_uuid
