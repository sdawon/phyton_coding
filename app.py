import streamlit as st
# 수정1 
from database.runtime import initialize_database

# 수정2 화면 출력이 시작되기 전에 데이터베이스 초기화 및 버전 가져오기
schema_version = initialize_database()


st.set_page_config(
    page_title="연구행정 효율화 프로그램",
    page_icon="📋",
    layout="wide",
)

st.title("📋 연구행정 효율화 프로그램")
st.success("개발 환경이 정상적으로 연결되었습니다.")

st.subheader("현재 개발 단계")
st.write("0단계 — Windows 개발 환경 및 Streamlit 실행 확인")

st.subheader("기술 구성")
st.write("- Python 3.11")
st.write("- Streamlit")
st.write("- SQLite + SQLAlchemy")
st.write("- 로컬 1인 사용")
st.caption(f"데이터베이스 스키마 버전: {schema_version}")
