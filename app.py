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
    
    if any(word in traits for word in ["논리", "분석", "문제 해결", "수학", "과학"]):
        major = "💻 컴퓨터공학과"
        description = (
            "컴퓨터공학과는 소프트웨어 개발, 알고리즘, 데이터 분석, 인공지능 등 컴퓨터 관련 기술을 배우는 학과예요. 🖥️\n"
            "학생들은 프로그래밍, 문제 해결, 프로젝트 수행 등을 통해 논리적 사고와 창의력을 키워요. 🚀\n"
            "졸업 후에는 소프트웨어 개발자, 데이터 분석가, AI 연구원 등 다양한 IT 분야로 진출할 수 있어요. 🎯"
        )
        return major, description

    elif any(word in traits for word in ["사람", "도움", "교류", "상담", "심리", "공감"]):
        major = "🧠 심리학과"
        description = (
            "심리학과는 인간의 마음과 행동을 이해하고 분석하는 학과예요. 💬\n"
            "인지, 정서, 발달, 상담 등 다양한 심리 이론을 배우고 실험과 연구를 통해 사람을 이해합니다. 🔬\n"
            "졸업 후에는 상담사, HR 전문가, 교육자, 연구원 등 사람과 관련된 다양한 분야에서 활동할 수 있어요. 🌱"
        )
        return major, description

    elif any(word in traits for word in ["창의", "그림", "디자인", "예술", "색감", "아이디어"]):
        major = "🎨 디자인학과"
        description = (
            "디자인학과는 시각적 표현과 창의력을 활용해 다양한 디자인을 배우는 학과예요. 🖌️\n"
            "그래픽 디자인, 산업 디자인, UX/UI, 패션, 영상 등 실무 프로젝트를 통해 아이디어를 구현합니다. ✨\n"
            "졸업 후에는 디자이너, UX/UI 전문가, 영상 제작자, 패션 디자이너 등 창의적인 직업으로 진출할 수 있어요. 🌟"
        )
        return major, description

    elif any(word in traits for word in ["자연", "실험", "연구", "생명", "화학", "물리", "분석"]):
        major = "🔬 생명과학과"
        description = (
            "생명과학과는 생물과 자연 현상을 연구하며 실험과 분석을 통해 이해하는 학과예요. 🧬\n"
            "세포, 유전, 생태, 분자생물학 등 다양한 지식을 배우고 연구 실험을 통해 과학적 탐구 능력을 키워요. 🧪\n"
            "졸업 후에는 연구원, 생명공학 전문가, 환경 분석가, 의학 관련 분야 등으로 진출할 수 있어요. 🌿"
        )
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
