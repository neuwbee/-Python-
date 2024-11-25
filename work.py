import streamlit as st

# 직업 데이터
JOB_DATA = [
    {"직업 이름": "데이터 분석가", "회사 이름": "A회사", "지역": "서울"},
    {"직업 이름": "프로세스 엔지니어", "회사 이름": "B회사", "지역": "경기도"},
    {"직업 이름": "물류 전문가", "회사 이름": "C회사", "지역": "부산"},
    {"직업 이름": "인공지능 연구원", "회사 이름": "D회사", "지역": "서울"},
    {"직업 이름": "프로덕트 매니저", "회사 이름": "E회사", "지역": "서울"},
]

# 검색하기 함수
def search_jobs(query):
    query = query.lower().strip()  # 입력값을 소문자로 바꾸고 앞뒤 공백 제거
    return [
        job for job in JOB_DATA
        if query in job["직업 이름"].lower() or query in job["회사 이름"].lower() or query in job["지역"].lower()
    ]

# 앱 시작
def main():
    st.title("직업 찾기 도우미")
    st.write("원하는 직업, 회사, 지역을 입력하고 검색해보세요!")

    # 검색창
    search_query = st.text_input("검색어를 입력하세요 (예: 서울, 데이터 분석가):")
    if st.button("검색하기"):
        if search_query:
            results = search_jobs(search_query)
            if results:
                st.write("다음 직업을 찾았어요!")
                for job in results:
                    st.write(f"- 직업: {job['직업 이름']}, 회사: {job['회사 이름']}, 지역: {job['지역']}")
            else:
                st.write("결과가 없어요. 다른 검색어를 입력해보세요!")
        else:
            st.warning("검색어를 입력해주세요.")

if __name__ == "__main__":
    main()
