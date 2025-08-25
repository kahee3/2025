import streamlit as st

# =======================
# 🌟 CSS 스타일 적용
# =======================
st.markdown(
    """
    <style>
    /* 전체 배경 */
    .stApp {
        background: linear-gradient(135deg, #74ebd5 0%, #ACB6E5 100%);
        background-attachment: fixed;
        color: #ffffff;
        font-family: 'Arial', sans-serif;
    }

    /* 버튼 스타일 */
    .stButton>button {
        background-color: #ff6f61;
        color: white;
        font-size: 18px;
        border-radius: 12px;
        padding: 10px 25px;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff3b2e;
        transform: scale(1.05);
    }

    /* 입력창 스타일 */
    .stTextArea>div>div>textarea {
        background-color: rgba(255, 255, 255, 0.15);
        color: #ffffff;
        border-radius: 10px;
        font-size: 16px;
        padding: 10px;
    }

    /* 카드 느낌의 결과 박스 */
    .stSuccess, .stInfo, .stWarning {
        border-radius: 15px;
        padding: 20px;
        background: rgba(255, 255, 255, 0.2);
        color: white;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =======================
# 앱 제목
# =======================
st.title("🎓✨ 성향 기반 학과 추천 앱 ✨")
st.write("자신의 성격이나 평소 특성을 작성하면, 적합한 학과와 상세 설명을 예쁘게 알려드려요! 🌈")

# =======================
# 사용자 입력
# =======================
user_traits = st.text_area("💡 당신의 성격이나 평소 특성을 적어주세요:", "")

# =======================
# 학과 추천 함수 (이모티콘 포함)
# =======================
def recommend_major(traits):
    traits = traits.lower()
    
     # IT/공학
    if any(word in traits for word in ["논리", "분석", "수학", "프로그래밍"]):
        return "💻 컴퓨터공학과", "컴퓨터공학과는 소프트웨어 개발, 알고리즘, 인공지능 등을 배우는 학과예요. 🖥️"
    elif any(word in traits for word in ["전자", "회로", "기계", "로봇"]):
        return "🤖 전자/로봇공학과", "로봇, 전자회로, 자동화 시스템 등을 배우며 공학적 문제 해결 능력을 키워요."

    # 자연과학/생명
    elif any(word in traits for word in ["생명", "연구", "실험", "화학", "물리"]):
        return "🔬 생명과학과", "생물과 자연 현상을 연구하고 실험하며 과학적 탐구 능력을 키우는 학과예요. 🧬"
    elif any(word in traits for word in ["수학", "통계", "분석"]):
        return "📊 수학/통계학과", "수학적 사고와 통계 분석 능력을 활용하여 다양한 문제를 해결하는 학과예요."

    # 인문/사회
    elif any(word in traits for word in ["사람", "심리", "상담", "교류"]):
        return "🧠 심리학과", "인간의 마음과 행동을 이해하고 분석하는 학과예요. 💬"
    elif any(word in traits for word in ["사회", "정책", "연구", "봉사"]):
        return "🌍 사회학과", "사회 구조와 문제를 연구하고 사회 개선 방안을 탐구하는 학과예요."
    elif any(word in traits for word in ["교육", "아이", "학습", "가르침"]):
        return "📚 교육학과", "교육 방법과 학습 과정을 연구하며 교사나 교육 컨설턴트로 진출할 수 있어요."
    elif any(word in traits for word in ["경제", "금융", "사업", "관리"]):
        return "💰 경영/경제학과", "기업 운영, 재무, 마케팅 등을 배우며 전략적 사고를 기르는 학과예요."
    elif any(word in traits for word in ["법", "규칙", "정의", "분쟁"]):
        return "⚖️ 법학과", "법과 정의, 사회 규범을 배우며 변호사, 판사, 법률 전문가로 진출할 수 있어요."
    elif any(word in traits for word in ["역사", "문화", "과거"]):
        return "🏛️ 역사학과", "인류의 과거 사건과 문화를 연구하고 분석하는 학과예요."
    elif any(word in traits for word in ["언어", "문학", "커뮤니케이션"]):
        return "📝 언어/문학과", "언어와 글, 문학을 연구하며 번역, 교육, 커뮤니케이션 분야로 진출할 수 있어요."
    
    # 예술
    elif any(word in traits for word in ["창의", "그림", "디자인", "예술"]):
        return "🎨 디자인/예술학과", "시각적 표현과 창의력을 활용하여 다양한 디자인을 배우는 학과예요."
    elif any(word in traits for word in ["음악", "연주", "작곡"]):
        return "🎵 음악학과", "음악 이론, 작곡, 연주를 배우며 음악적 표현 능력을 키우는 학과예요."
    elif any(word in traits for word in ["체육", "운동", "건강"]):
        return "🏋️‍♂️ 체육학과", "운동, 스포츠 과학, 건강 관리 등을 배우며 체력과 지도 능력을 향상시켜요."

    # 의학/보건
    elif any(word in traits for word in ["의학", "치료", "건강", "병원", "환자"]):
        return "🏥 의학/의예과", "인체와 질병을 연구하고 치료 방법을 배우는 학과예요. 💉"
    elif any(word in traits for word in ["약", "약학", "화학", "연구"]):
        return "💊 약학과", "약물 연구, 개발, 관리 등 약학 전반을 배우는 학과예요."

    # 환경/자연
    elif any(word in traits for word in ["환경", "자연", "지구", "보호", "지속"]):
        return "🌱 환경과학과", "지구 환경과 생태계를 연구하고 문제 해결 능력을 기르는 학과예요."

        return major, description

    else:
        return "❓ 추천 학과 없음", "입력하신 특성으로 정확한 학과를 추천하기 어려워요. 좀 더 구체적으로 작성해보세요! 📝"

# =======================
# 추천 버튼
# =======================
if st.button("✨ 추천받기 ✨"):
    if user_traits.strip() == "":
        st.warning("⚠️ 먼저 특성을 입력해주세요!")
    else:
        major, description = recommend_major(user_traits)
        st.success(f"✅ 당신에게 추천하는 학과: {major}")
        st.info(description)
