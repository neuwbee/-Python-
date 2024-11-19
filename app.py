import streamlit as st
import json

# 샘플 직무 데이터
JOB_DATA = [
    {"name": "데이터 분석가", "required_skills": ["Python", "SQL", "데이터 분석"], "industry": "IT"},
    {"name": "프로세스 엔지니어", "required_skills": ["Lean", "6시그마", "프로세스 개선"], "industry": "제조"},
    {"name": "물류 전문가", "required_skills": ["ERP", "공급망", "물류 관리"], "industry": "물류"}
]

# 직무 추천 함수
def recommend_jobs(interests, skills, jobs):
    recommendations = []
    for job in jobs:
        if any(skill in job["required_skills"] for skill in skills):
            recommendations.append(job)
    return recommendations

# Streamlit 애플리케이션
def main():
    st.title("졸업 후 진로 설계 도우미")
    st.write("산업경영공학 전공자를 위한 진로 탐색 및 취업 도우미")

    # 섹션 1: 자기 분석
    st.header("1. 자기 분석")
    interests = st.text_input("관심사를 입력하세요 (쉼표로 구분):", "")
    skills = st.text_input("강점을 입력하세요 (쉼표로 구분):", "")
    
    if st.button("분석 시작"):
        user_data = {
            "interests": [interest.strip() for interest in interests.split(",")],
            "skills": [skill.strip() for skill in skills.split(",")]
        }
        st.success("자기 분석 완료!")
        st.write("입력된 관심사:", user_data["interests"])
        st.write("입력된 강점:", user_data["skills"])

        # 섹션 2: 직무 추천
        st.header("2. 직무 추천")
        recommendations = recommend_jobs(user_data["interests"], user_data["skills"], JOB_DATA)
        if recommendations:
            st.subheader("추천 직무")
            for job in recommendations:
                st.write(f"- **{job['name']}** (산업: {job['industry']})")
                st.write(f"  필요한 기술: {', '.join(job['required_skills'])}")
        else:
            st.write("적합한 직무를 찾지 못했습니다. 입력 데이터를 확인해보세요.")

    # 섹션 3: 취업 준비 체크리스트
    st.header("3. 취업 준비 체크리스트")
    if "tasks" not in st.session_state:
        st.session_state.tasks = []

    new_task = st.text_input("추가할 준비 항목:")
    if st.button("항목 추가"):
        if new_task:
            st.session_state.tasks.append({"task": new_task, "completed": False})
            st.success("항목이 추가되었습니다!")
        else:
            st.warning("항목을 입력하세요.")

    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.write(f"- {task['task']} ({'완료' if task['completed'] else '미완료'})")
        with col2:
            if not task["completed"] and st.button("완료", key=f"complete-{i}"):
                st.session_state.tasks[i]["completed"] = True
                st.success(f"'{task['task']}' 완료!")

# 실행
if __name__ == "__main__":
    main()
