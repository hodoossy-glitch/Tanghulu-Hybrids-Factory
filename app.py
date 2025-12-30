import streamlit as st
import google.generativeai as genai

# 1. 페이지 설정: 오팔 미디어 페이지 스타일 (Surreal Elegance)
st.set_page_config(page_title="Hybrid Creature Gallery", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0b0e14; color: #ffffff; }
    h1 { font-family: 'Montserrat', sans-serif; text-align: center; color: #f0f0f0; }
    .gallery-card { background: #161b22; padding: 25px; border-radius: 20px; border: 1px solid #30363d; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 2. API 설정 및 모델 로드
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
    # 무료 등급에서 가장 안정적인 모델 경로를 직접 지정합니다.
    model = genai.GenerativeModel('models/gemini-1.5-flash')
except Exception as e:
    st.error(f"설정 오류: {e}")

# 3. 입력 섹션 (Opal Step 1)
st.markdown("<h1>✨ Hybrid Creature Media Gallery</h1>", unsafe_allow_html=True)
user_input = st.text_input("Describe your hybrid creature", placeholder="Violin Koala, Taxi Cat, Fridge Hippo...")

# 4. 생성 로직 (들여쓰기 및 SyntaxError 완벽 해결 버전)
if st.button("🚀 Generate Artwork"):
    if user_input:
        with st.spinner("오팔 엔진이 크리처를 설계 중입니다..."):
            try:
                # [Opal Step 2 & 3: Image Prompt]
                # try 블록 바로 아래에 실제 코드가 있어야 에러가 나지 않습니다.
                img_p = (
                    f"Expert prompt for '{user_input}': "
                    "1. Replace animal parts with object components. "
                    "2. Apply thick, ultra-glossy, squishy Tanghulu-like glaze to all surfaces. "
                    "3. Photorealistic and surreal. IMPORTANT: Generate exactly one image."
                )
                img_res = model.generate_content(img_p).text

                #
