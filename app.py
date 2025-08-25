import streamlit as st
import pandas as pd

# ------------------------------
# 질병 데이터 예시 (향후 CSV로 확장 가능)
# ------------------------------
disease_data = {
    "질병명": ["감기", "당뇨병", "우울증", "고혈압", "천식"],
    "분류": ["감염병", "만성질환", "정신건강", "만성질환", "호흡기질환"],
    "증상": [
        "콧물, 재채기, 기침",
        "혈당 상승, 잦은 갈증, 피로",
        "우울감, 무기력, 수면 장애",
        "혈압 상승, 두통, 어지럼증",
        "호흡 곤란, 기침, 가슴 답답함"
    ],
    "치료법": [
        "휴식, 수분 섭취, 해열제 복용",
        "식이요법, 운동, 인슐린·약물 치료",
        "심리 상담, 약물 치료, 규칙적인 생활",
        "염분 제한, 운동, 항고혈압제 복용",
        "흡입제 사용, 알레르기 요인 제거"
    ],
    "예방": [
        "손 씻기, 마스크 착용",
        "식습관 관리, 규칙적 운동",
        "스트레스 관리, 사회적 교류 유지",
        "저염식, 체중 관리",
        "알레르기 유발 물질 피하기"
    ]
}

df = pd.DataFrame(disease_data)

# ------------------------------
# Streamlit 앱 UI
# ------------------------------
st.set_page_config(page_title="🩺 질병별 치료 가이드", layout="centered")

st.title("🩺 질병별 치료 가이드")
st.write("궁금한 질병을 검색하거나, 질병 분류별로 찾아보세요!")

# 검색 기능
search = st.text_input("🔍 질병명을 입력하세요 (예: 감기, 당뇨병)").strip()

# 분류 필터
category = st.selectbox(
    "📂 질병 분류 선택",
    options=["전체"] + sorted(df["분류"].unique())
)

# ------------------------------
# 검색 및 필터 처리
# ------------------------------
filtered_df = df.copy()

if search:
    filtered_df = filtered_df[filtered_df["질병명"].str.contains(search, case=False)]
if category != "전체":
    filtered_df = filtered_df[filtered_df["분류"] == category]

# ------------------------------
# 결과 출력
# ------------------------------
if not filtered_df.empty:
    for _, row in filtered_df.iterrows():
        st.subheader(f"🧾 {row['질병명']}")
        st.markdown(f"**분류:** {row['분류']}")
        st.markdown(f"**증상:** {row['증상']}")
        st.markdown(f"**치료법:** {row['치료법']}")
        st.markdown(f"**예방:** {row['예방']}")
        st.divider()
else:
    st.warning("⚠️ 검색 결과가 없습니다. 다른 키워드를 입력해보세요.")

# ------------------------------
# 푸터
# ------------------------------
st.caption("💡 본 정보는 일반적인 건강 가이드이며, 정확한 진단 및 치료는 의료 전문가와 상담하세요.")

    
