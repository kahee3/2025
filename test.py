import streamlit as st

# =======================
# 🌟 CSS 스타일 적용 (배경 이모티콘 추가)
# =======================
st.markdown(
    """
    <style>
    /* 전체 배경: 그라데이션 + 이모티콘 패턴 */
    .stApp {
        background: linear-gradient(135deg, #74ebd5 0%, #ACB6E5 100%);
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='50' height='50'%3E%3Ctext x='0' y='15' font-size='15'%3E👩‍⚕️👨‍💻👩‍🏫👨‍🔬👩‍🎨👨‍🚒👩‍💼👨‍🎓%3C/text%3E%3C/svg%3E");
        background-repeat: repeat;
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
# 학과 추천 함수 (예시)
# =======================
def recommend_major(traits):
    traits = traits.lower()
    
    if any(word in traits for word in ["논리", "분석", "문제 해결", "수학", "과학"]):
        major = "💻 컴퓨터공학과"
        description = (
            "컴퓨터공학과는 소프트웨어 개발, 알고리즘, 데이터 분석, 인공지능 등 컴퓨터 관련 기술을 배우는 학과예요. 🖥️\n"
            "졸업 후에는 소프트웨어 개발자, 데이터 분석가, AI 연구원 등 다양한 IT 분야로 진출할 수 있어요. 🎯"
        )
        return major, description
    elif any(word in traits for word in ["사람", "도움", "교류", "상담", "심리", "공감"]):
        major = "🧠 심리학과"
        description = (
            "심리학과는 인간의 마음과 행동을 이해하고 분석하는 학과예요. 💬\n"
            "졸업 후에는 상담사, HR 전문가, 교육자, 연구원 등 사람과 관련된 다양한 분야에서 활동할 수 있어요. 🌱"
        )
        return major, description
    elif any(word in traits for word in ["창의", "그림", "디자인", "예술", "색감", "아이디어"]):
        major = "🎨 디자인학과"
        description = (
            "디자인학과는 시각적 표현과 창의력을 활용해 다양한 디자인을 배우는 학과예요. 🖌️\n"
            "졸업 후에는 디자이너, UX/UI 전문가, 영상 제작자, 패션 디자이너 등 창의적인 직업으로 진출할 수 있어요. 🌟"
        )
        return major, description
    else:
        return "❓ 추천 학과 없음", "입력하신 특성으로 정확한 학과를 추천하기 어려워요. 📝"

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

