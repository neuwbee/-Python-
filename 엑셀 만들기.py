from faker import Faker
import pandas as pd
import random

# Faker 초기화
fake = Faker('ko_KR')  # 한국어 데이터 생성
Faker.seed(42)

# 샘플 데이터
job_titles = ["데이터 분석가", "프로세스 엔지니어", "물류 전문가", "인공지능 연구원", "프로덕트 매니저", "웹 개발자", "시스템 엔지니어", "마케팅 매니저"]
skills = [
    ["Python", "SQL", "데이터 분석"],
    ["Lean", "6시그마", "프로세스 개선"],
    ["ERP", "공급망", "물류 관리"],
    ["머신러닝", "딥러닝", "Python"],
    ["프로젝트 관리", "커뮤니케이션", "UX 설계"],
    ["HTML", "CSS", "JavaScript"],
    ["Linux", "서버 관리", "네트워크"],
    ["마케팅 전략", "데이터 분석", "브랜드 관리"]
]
fields = ["IT", "제조", "물류", "마케팅", "디자인", "금융", "교육"]
employment_types = ["정규직", "계약직", "인턴", "프리랜서"]
locations = ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "경기도"]
certifications = [
    "정보처리기사", "웹 개발자 자격증", "SQL 전문가", "ERP 컨설턴트", "인공지능 전문가", 
    "리더십 자격증", "빅데이터 분석기사", "마케팅 전문가", "프로젝트 관리 전문가(PMP)"
]

# 랜덤 채용 정보 생성 (300개)
jobs = []
for _ in range(300):
    idx = random.randint(0, len(job_titles) - 1)
    jobs.append({
        "직업 이름": job_titles[idx],
        "필요한 기술": ", ".join(random.sample(skills[idx], random.randint(1, 3))),
        "분야": random.choice(fields),
        "회사 이름": fake.company(),
        "근무 지역": random.choice(locations),
        "연봉": f"{random.randint(3000, 8000)}만 원",
        "고용 형태": random.choice(employment_types),
        "자격증": random.choice(certifications)  # 자격증 추가
    })

# 데이터프레임으로 변환
df = pd.DataFrame(jobs)

# 엑셀 파일로 저장
file_path = '채용정보_with_자격증.xlsx'  # 로컬 경로
df.to_excel(file_path, index=False, engine='openpyxl')

print(f"파일이 생성되었습니다: {file_path}")
