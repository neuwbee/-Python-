import streamlit as st
import pandas as pd

# 엑셀에서 데이터 불러오기
@st.cache_data
def load_job_data(file_path):
    return pd.read_excel(file_path)

# 직업 추천: 관심사와 강점에 맞는 직업 추천
def recommend_jobs(interests, skills, job_data):
    # 관심사와 기술을 모두 소문자로 변환
    interests = [i.lower() for i in interests]
    skills = [s.lower() for s in skills]

    # 조건에 맞는 직업만 필터링
    filtered_jobs = job_data[
        job_data["필요한 기술"].str.lower().apply(lambda tech: any(skill in tech for skill in skills)) |
        job_data["분야"].str.lower().apply(lambda field: any(interest in field for interest in interests))
    ]

    return filtered_jobs

# 메인 함수
def main():
    st.title("산업경영공학과 학생들을 위한 직업 검색 도우미 🕵️‍♀️")
    st.write("원하는 직업을 검색하고 계획을 세워보세요!")

    # 데이터 로드
    file_path = "채용정보_with_자격증.xlsx"
    job_data = load_job_data(file_path)

    # 1. 검색하기 섹션
    st.header("1. 원하는 직업 찾기")
    search = st.text_input("찾고 싶은 직업, 기술, 근무 지역을 적어보세요!")
    if st.button("검색"):
        if search:
            results = job_data[
                job_data.apply(lambda row: search.lower() in row.to_string().lower(), axis=1)
            ]
            if not results.empty:
                st.subheader("검색 결과")
                st.dataframe(results)
            else:
                st.write("찾는 직업이 없습니다. 다시 검색해보세요!")
        else:
            st.warning("검색어를 입력해주세요.")

    # 2. 관심사와 강점으로 직업 추천받기
    st.header("2. 관심사와 강점으로 직업 추천받기")
    interests = st.text_input("관심 있는 분야를 적어보세요 (쉼표로 구분):", "")
    skills = st.text_input("내가 잘하는 것을 적어보세요 (쉼표로 구분):", "")
    if st.button("추천받기"):
        if interests.strip() and skills.strip():
            user_interests = [i.strip() for i in interests.split(",")]
            user_skills = [s.strip() for s in skills.split(",")]
            recommendations = recommend_jobs(user_interests, user_skills, job_data)
            if not recommendations.empty:
                st.subheader("추천받은 직업")
                st.dataframe(recommendations)
            else:
                st.write("추천할 직업이 없습니다. 관심사와 강점을 다시 입력해보세요!")
        else:
            st.warning("관심사와 강점을 모두 적어주세요.")

    # 3. 해야 할 일 정리하기
    st.header("3. 해야 할 일 정리하기")
    # 세션 상태 초기화
    if "tasks" not in st.session_state:
        st.session_state.tasks = []

    # 새로운 할 일 입력
    new_task = st.text_input("해야 할 일을 적어보세요:")
    if st.button("추가"):
        if new_task:
            st.session_state.tasks.append({"할 일": new_task, "완료": False})
            st.success(f"'{new_task}' 추가 완료!")
        else:
            st.warning("할 일을 입력해주세요.")

    # 할 일 목록 보여주기
    st.subheader("현재 해야 할 일 목록")
    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.write(task["할 일"])
        with col2:
            if st.button(f"완료 {i}", key=f"complete_{i}"):
               st.session_state.tasks.pop(i)
               

# 실행
if __name__ == "__main__":
    main()
