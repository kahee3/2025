import streamlit as st
import pandas as pd

# ------------------------------
# 질병 데이터 + 이모지
# ------------------------------
disease_data = [
    {"질병명": "감기 🤧", "분류": "감염병", "증상": "콧물, 재채기, 기침",
     "치료법": "휴식, 수분 섭취, 해열제 복용", "예방": "손 씻기, 마스크 착용"},
    {"질병명": "당뇨병 🍬", "분류": "만성질환", "증상": "혈당 상승, 잦은 갈증, 피로",
     "치료법": "식이요법, 운동, 인슐린·약물 치료", "예방": "식습관 관리, 규칙적 운동"},
    {"질병명": "우울증 😔", "분류": "정신건강", "증상": "우울감, 무기력, 수면 장애",
     "치료법": "심리 상담, 약물 치료, 규칙적인 생활", "예방": "스트레스 관리, 사회적 교류 유지"},
    {"질병명": "고혈압 💓", "분류": "만성질환", "증상": "혈압 상승, 두통, 어지럼증",
     "치료법": "염분 제한, 운동, 항고혈압제 복용", "예방": "저염식, 체중 관리"},
    {"질병명": "천식 🌬️", "분류": "호흡기질환", "증상": "호흡 곤란, 기침, 가슴 답답함",
     "치료법": "흡입제 사용, 알레르기 요인 제거", "예방": "알레르기 유발 물질 피하기"},
    {"질병명": "편두통 🤯", "분류": "신경질환", "증상": "두통, 빛·소리에 민감",
     "치료법": "진통제, 충분한 휴식, 카페인 섭취 조절", "예방": "스트레스 관리, 수면 패턴 유지"}
]
df = pd.DataFrame(disease_data)

# ------------------------------
# 페이지 설정
# ------------------------------
st.set_page_config(page_title="🏥 병원 스타일 질병 가이드", layout="wide")

# ------------------------------
# 배경 이미지 패턴 + CSS
# ------------------------------
st.markdown("""
<style>
body {
    background-color: #e0f7fa;
    background-image: url('https://i.ibb.co/3fK0H6r/medical-pattern.png');
    background-repeat: repeat;
    background-size: 100px 100px;
}

/* 타이틀 */
.title {
    font-size: 48px;
    font-weight: 900;
    text-align: center;
    color: #00796b;
    padding: 20px;
    margin-bottom: 20px;
    text-shadow: 1px 1px 5px rgba(0,0,0,0.1);
}

/* 카드 스타일 */
.card {
    background: rgba(255,255,255,0.85);
    border-radius: 20px;
    padding: 20px;
    margin: 15px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 25px rgba(0,0,0,0.25);
}

/* 카드 텍스트 */
.card h3 { color: #00796b; font-weight: 700; }
.card p { color: #004d40; font-size: 15px; }

/* 푸터 */
.footer {
    text-align: center;
    color: #004d40;
    font-size: 14px;
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------
# 타이틀
# ------------------------------
st.markdown('<div class="title">🏥 병원 느낌 질병 가이드</div>', unsafe_allow_html=True)
st.write("💡 질병 검색과 분류 필터로 치료 정보를 확인하세요.")

# ------------------------------
# 검색/필터
# ------------------------------
search = st.text_input("🔍 질병명을 입력하세요 (예: 감기, 우울증)").strip()
category = st.selectbox("📂 질병 분류 선택", options=["전체"] + sorted(df["분류"].unique()))

filtered_df = df.copy()
if search:
    filtered_df = filtered_df[filtered_df["질병명"].str.contains(search, case=False)]
if category != "전체":
    filtered_df = filtered_df[filtered_df["분류"] == category]

# ------------------------------
# 카드 출력 (2열 레이아웃)
# ------------------------------
cols = st.columns(2)
for i, (_, row) in enumerate(filtered_df.iterrows()):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="card">
            <h3>{row['질병명']}</h3>
            <p><strong>📌 분류:</strong> {row['분류']}</p>
            <p><strong>🧾 증상:</strong> {row['증상']}</p>
            <p><strong>💊 치료법:</strong> {row['치료법']}</p>
            <p><strong>🛡 예방:</strong> {row['예방']}</p>
        </div>
        """, unsafe_allow_html=True)

if filtered_df.empty:
    st.warning("⚠️ 검색 결과가 없습니다. 다른 키워드를 입력해보세요!")

# ------------------------------
# 푸터
# ------------------------------
st.markdown('<div class="footer">💡 본 정보는 일반 건강 가이드이며, 정확한 진단은 전문가와 상담하세요.</div>', unsafe_allow_html=True)

