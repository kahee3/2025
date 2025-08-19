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
