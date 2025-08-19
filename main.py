import streamlit as st

# MBTI별 직업 추천 데이터
job_recommendations = {
    "INTJ": ["전략기획자", "데이터 사이언티스트", "연구원"],
    "ENTP": ["기업가", "마케팅 기획자", "컨설턴트"],
    "INFJ": ["상담가", "작가", "교사"],
    "ENFP": ["광고 기획자", "이벤트 플래너", "방송 PD"],
    # 필요에 따라 추가
}

st.set_page_config(page_title="MBTI 직업 추천", page_icon="✨", layout="centered")

# 메인 화면
st.title("✨ MBTI 기반 직업 추천 웹사이트")
st.write("당신의 MBTI에 맞는 직업을 찾아보세요!")

# MBTI 입력
mbti = st.selectbox(
    "당신의 MBTI를 선택하세요:",
    list(job_recommendations.keys())
)

if st.button("추천 직업 보기"):
    st.subheader(f"당신의 MBTI: {mbti}")
    st.write("✅ 추천 직업 리스트:")

    for job in job_recommendations[mbti]:
        st.markdown(f"- **{job}**")

    st.success("자신에게 맞는 진로를 탐색해 보세요!")
    import streamlit as st

# --- 기본 설정 ---
st.set_page_config(page_title="MBTI 직업 추천", page_icon="💼", layout="centered")

# --- 직업 추천 데이터 ---
job_recommendations = {
    "INTJ": {
        "desc": "🧠 전략적 사고와 계획을 잘 세우는 유형",
        "jobs": ["📊 데이터 사이언티스트", "📈 전략기획자", "🔬 연구원"]
    },
    "ENTP": {
        "desc": "💡 창의적이고 새로운 도전을 즐기는 유형",
        "jobs": ["🚀 기업가", "📣 마케팅 기획자", "🧑‍💼 컨설턴트"]
    },
    "INFJ": {
        "desc": "🌱 깊이 있는 통찰과 배려심을 가진 유형",
        "jobs": ["🧑‍🏫 교사", "💬 상담가", "✍️ 작가"]
    },
    "ENFP": {
        "desc": "🔥 열정적이고 사람들과 어울리기를 좋아하는 유형",
        "jobs": ["🎤 방송 PD", "🎉 이벤트 플래너", "🖌️ 광고 기획자"]
    },
    "ISTJ": {
        "desc": "📚 책임감 있고 신뢰할 수 있는 유형",
        "jobs": ["⚖️ 판사", "🧑‍💼 회계사", "🏢 공무원"]
    },
    "ESFP": {
        "desc": "🎶 에너지 넘치고 활발한 유형",
        "jobs": ["🎬 배우", "🎶 가수", "🎉 엔터테이너"]
    },
    # 필요에 따라 계속 추가 가능
}

# --- 메인 화면 ---
st.markdown(
    """
    <div style='text-align: center;'>
        <h1>✨ MBTI 기반 직업 추천 ✨</h1>
        <p>당신의 성격 유형에 맞는 직업을 찾아보세요! 🎯</p>
    </div>
    """,
    unsafe_allow_html=True
)

# --- MBTI 입력 ---
mbti = st.selectbox(
    "👉 당신의 MBTI를 선택하세요:",
    list(job_recommendations.keys())
)

# --- 결과 버튼 ---
if st.button("🔎 추천 직업 보기"):
    data = job_recommendations[mbti]

    st.markdown(f"## 🪪 당신의 MBTI: **{mbti}**")
    st.info(data["desc"])

    st.markdown("### 💼 추천 직업 리스트:")

    # 카드 스타일 출력
    for job in data["jobs"]:
        st.markdown(
            f"""
            <div style="
                background-color:#f9f9f9;
                padding:15px;
                border-radius:15px;
                margin-bottom:10px;
                box-shadow:2px 2px 5px rgba(0,0,0,0.1);
                font-size:18px;">
                {job}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.success("🌟 나에게 맞는 진로를 찾아보는 여정이 시작됐어요! 🚀")

