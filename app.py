import streamlit as st
import google.generativeai as genai

# 1. 페이지 설정: 오팔 Surreal Elegance 스타일 반영
st.set_page_config(page_title="Hybrid Creature Media Gallery", layout="wide")

# 스타일 설정: 갤러리풍 다크 테마 디자인
st.markdown("""
    <style>
    .main { background-color: #0b0e14; color: #ffffff; }
    h1 { font-family: 'Montserrat', sans-serif; text-align: center; color: #f0f0f0; margin-bottom: 30px; }
    .gallery-card { background: #161b22; padding: 25px; border-radius: 20px; border: 1px solid #30363d; margin-bottom: 20px; }
    .stButton>button { width: 100%; border-radius: 10px; background-color: #238636; color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 2. API 설정 및 모델 로드 (404 오류 방지)
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
    # v1beta 등 모든 버전에서 가장 안정적인 모델 식별자를 사용합니다.
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"⚠️ API 설정 오류: {e}")

# 3. 앱 헤더 및 입력 (Opal Step 1 반영)
st.markdown("<h1>✨ Hybrid Creature Media Gallery</h1>", unsafe_allow_html=True)
user_input = st.text_input("Describe your hybrid creature", placeholder="Violin Koala, Taxi Cat, Fridge Hippo...")

# 4. 실행 로직 (SyntaxError 해결 및 오팔 로직 이식)
if st.button("🚀 Generate Artwork"):
    if user_input:
        with st.spinner("오팔 엔진이 크리처를 설계 중입니다..."):
            try:
                # [Opal Step 2 & 3: Image Prompt 생성]
                # try 블록 바로 아래에 실제 실행 코드를 배치하여 문법 에러를 해결합니다.
                img_p = (
                    f"Expert prompt for '{user_input}': "
                    "1. Replace animal parts with object components. "
