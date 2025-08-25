import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="질병별 치료 가이드",
    page_icon="🏥",
    layout="wide"
)

# 병원 느낌 CSS
st.markdown("""
    <style>
        body {
            background-image: url('https://images.unsplash.com/photo-1588774066925-6e32f0c78f80?auto=format&fit=crop&w=1950&q=80');
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(240, 248, 255, 0.6);
            z-index: -1;
        }
        .title {
            text-align: center;
            font-size: 50px;
            color: #0f4c81;
            text-shadow: 1px 1px 6px rgba(255,255,255,0.8);
            margin-bottom: 20px;
            font-weight: bold;
        }
        .card {
            background: rgba(255, 255, 255, 0.85);
            border-radius: 20px;
            padding: 30px;
            margin: 20px 0;
            box-shadow: 0 4px 25px rgba(0, 0, 0, 0.1);
        }
        .subtitle {
            font-size: 26px;
            color: #0f4c81;
            margin-bottom: 10px;
            font-weight: bold;
        }
        .list-item {
            font-size: 18px;
            padding: 5px 0;
            color: #333;
        }
        .footer {
            text-align: center;
            font-size: 14px;
            color: #0f4c81;
            margin-top: 50px;
            opacity: 0.8;
        }
    </style>
    <div class="overlay"></div>
""", unsafe_allow_html=True)

# 제목
st.markdown('<div class="title">🏥 질병별 치료 가이드</div>', unsafe_allow_html=True)
st.write("전문 의료 가이드와 함께 건강을 지켜보세요. 질병을 선택하면 치료법과 예방 팁을 확인할 수 있습니다. 🩺")

# 질병 데이터
disease_data = {
    "감기 🤧": {
        "설명": "감기는 흔한 바이러스 감염으로 코막힘, 기침, 인후통 등이 동반됩니다.",
        "치료": [
            "💧 충분한 수분 섭취와 휴식",
            "💊 진통제 또는 해열제 복용",
            "🩺 고열 또는 증상 악화 시 의사 진료"
        ],
        "예방": "🧼 손을 자주 씻고 마스크 착용으로 감염을 예방하세요."
    },
    "고혈압 💓": {
        "설명": "고혈압은 혈압이 지속적으로 높아 심혈관 질환의 주요 원인이 됩니다.",
        "치료": [
            "🥗 저염식 식단 유지",
            "🏃 주 3회 이상 유산소 운동",
            "💊 처방받은 혈압약을 꾸준히 복용"
        ],
        "예방": "⚖️ 체중을 유지하고 스트레스 관리를 생활화하세요."
    },
    "당뇨병 🍬": {
        "설명": "당뇨병은 혈당 조절 능력이 저하되어 고혈당 상태가 지속되는 질환입니다.",
        "치료": [
            "🥗 탄수화물 조절 식단",
            "🩸 주기적인 혈당 측정",
            "💉 필요 시 인슐린 또는 약물 치료"
        ],
        "예방": "🚶 규칙적인 운동과 균형 잡힌 식습관을 유지하세요."
    },
    "위염 🤢": {
        "설명": "위 점막에 염증이 생겨 통증이나 속쓰림이 발생하는 질환입니다.",
        "치료": [
            "🍵 자극적인 음식과 음주 피하기",
            "⏰ 규칙적인 식사 습관 유지",
            "💊 제산제나 위장약 복용"
        ],
        "예방": "😌 스트레스를 줄이고 충분한 휴식을 취하세요."
    }
}

# 질병 선택
disease = st.selectbox("🔍 질병을 선택하세요", list(disease_data.keys()))

# 선택한 질병 데이터
info = disease_data[disease]

# 카드 스타일 출력
st.markdown(f"""
<div class="card">
    <div class="subtitle">📖 {disease} 정보</div>
    <p style="font-size:18px; color:#333;">{info['설명']}</p>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="card">
    <div class="subtitle">💡 치료 방법</div>
    {''.join([f"<div class='list-item'>{method}</div>" for method in info['치료']])}
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="card">
    <div class="subtitle">🛡 예방 팁</div>
    <p style="font-size:18px; color:#333;">{info['예방']}</p>
</div>
""", unsafe_allow_html=True)

# 푸터
st.markdown('<div class="footer">© 2025 건강 가이드 | 전문의 상담을 대신하지 않습니다 🏥</div>', unsafe_allow_html=True)

        
