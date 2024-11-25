import streamlit as st
import pandas as pd

# 직업 정보
JOB_DATA = [
    {
        "직업 이름": "데이터 분석가",
        "필요한 기술": ["Python", "SQL", "데이터 분석"],
        "분야": "IT",
        "회사 이름": "A회사",
        "근무 지역": "서울",
        "연봉": "4,000만 원",
        "고용 형태": "정규직",
        "직무 설명": "데이터를 분석해 중요한 정보를 찾는 일을 합니다."
    },
    {
        "직업 이름": "프로세스 엔지니어",
        "필요한 기술": ["Lean", "6시그마", "프로세스 개선"],
        "분야": "제조",
        "회사 이름": "B회사",
        "근무 지역": "경기도",
        "연봉": "5,000만 원",
        "고용 형태": "정규직",
        "직무 설명": "공장에서 일을 더 빠르고 효율적으로 만드는 일을 합니다."
    },
    {
        "직업 이름": "물류 전문가",
        "필요한 기술": ["ERP", "공급망", "물류 관리"],
        "분야": "물류",
        "회사 이름": "C회사",
        "근무 지역": "부산",
        "연봉": "4,500만 원",
        "고용 형태": "계약직",
        "직무 설명": "물건을 더 빠르고 저렴하게 이동시키는 일을 합니다."
    },
    {
        "직업 이름": "인공지능 연구원",
        "필요한 기술": ["Python", "머신러닝", "딥러닝"],
        "분야": "IT",
        "회사 이름": "D회사",
        "근무 지역": "서울",
        "연봉": "6,000만 원",
        "고용 형태": "정규직",
        "직무 설명": "AI 기술을 연구해 똑똑한 프로그램을 만듭니다."
    },
    {
        "직업 이름": "프로덕트 매니저",
        "필요한 기술": ["프로젝트 관리", "커뮤니케이션", "UX 설계"],
        "분야": "IT",
        "회사 이름": "E회사",
        "근무 지역": "서울",
        "연봉": "5,500만 원",
        "고용 형태": "정규직",
        "직무 설명": "제품을 기획하고 출시까지 관리하는 일을 합니다."
    },
]

# 검색하기: 원하는 직업이나 기술을 찾는 함수
def search_jobs(query):
    query = query.lower().strip()  # 검색어를 소문자로 바꾸고 공백을 없앰
    return [
        job for job in JOB_DATA
        if query in job["직업 이름"].lower() or
           query in job["회사 이름"].lower() or
           query in job["근무 지역"].lower() or
           any(query in skill.lower() for skill in job["필요한 기술"])
    ]

# 직업 추천: 관심사와 강점에 맞는 직업을 추천
def recommend_jobs(interests, skills):
    recommendations = []
    for job in JOB_DATA:
        if any(skill.lower() in [s.lower() for s in job["필요한 기술"]] for skill in skills) or \
           any(interest.lower() in job["분야"].lower() for interest in interests):
            recommendations.append(job)
    return recommendations

# 앱 시작
def main():
    st.title("직업 검색 도우미 🕵️‍♀️")
    st.write("원하는 직업을 찾고 계획을 세워보세요!")

    # 검색하기 섹션
    st.header("1. 원하는 직업 찾기")
    search_query = st.text_input("찾고 싶은 직업, 기술, 회사 이름, 근무 지역을 적어보세요!")
    if st.button("검색"):
        if search_query:
            results = search_jobs(search_query)
            if results:
                st.subheader("검색 결과")
                st.table(pd.DataFrame(results))
            else:
                st.write("찾는 직업이 없어요. 다시 검색해보세요!")
        else:
            st.warning("검색어를 입력해주세요.")

    # 관심사와 강점을 입력받아 추천하기
    st.header("2. 관심사와 강점으로 직업 추천받기")
    interests = st.text_input("관심 있는 분야를 적어보세요 (쉼표로 구분):", "")
    skills = st.text_input("내가 잘하는 것을 적어보세요 (쉼표로 구분):", "")
    if st.button("추천받기"):
        if interests.strip() and skills.strip():
            user_interests = [i.strip() for i in interests.split(",")]
            user_skills = [s.strip() for s in skills.split(",")]
            recommendations = recommend_jobs(user_interests, user_skills)
            if recommendations:
                st.subheader("추천받은 직업")
                st.table(pd.DataFrame(recommendations))
            else:
                st.write("추천할 직업이 없어요. 관심사와 강점을 다시 입력해보세요!")
        else:
            st.warning("관심사와 강점을 모두 적어주세요.")

    # 체크리스트 섹션
    st.header("3. 해야 할 일 정리하기")
    if "tasks" not in st.session_state:
        st.session_state.tasks = []

    new_task = st.text_input("해야 할 일을 적어보세요:")
    if st.button("추가"):
        if new_task:
            st.session_state.tasks.append({"할 일": new_task, "완료": False})
            st.success(f"'{new_task}' 추가 완료!")
        else:
            st.warning("할 일을 입력해주세요.")

    # 할 일 목록 보여주기
    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.write(f"- {task['할 일']} ({'완료됨' if task['완료'] else '미완료'})")
        with col2:
            if not task["완료"] and st.button("완료", key=f"complete-{i}"):
                st.session_state.tasks[i]["완료"] = True
                st.success(f"'{task['할 일']}' 완료 처리되었습니다!")

# 실행
if __name__ == "__main__":
    main()
