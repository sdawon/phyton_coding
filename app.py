import streamlit as st

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
