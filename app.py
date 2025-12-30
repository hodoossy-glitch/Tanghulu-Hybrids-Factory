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
    # v1beta 등 모든 버전에서 가장 잘 작동하는 모델명을 사용합니다.
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"⚠️ 설정 오류: {e}")

# 3. 앱 헤더 및 입력 (Opal Step 1 반영)
st.markdown("<h1>✨ Hybrid Creature Media Gallery</h1>", unsafe_allow_html=True)
user_input = st.text_input("Describe your hybrid creature", placeholder="Violin Koala, Taxi Cat, Fridge Hippo...")

# 4. 실행 로직 (모든 문법 에러 및 404 해결 버전)
if st.button("🚀 Generate Artwork"):
    if user_input:
        with st.spinner("오팔 엔진이 크리처를 설계 중입니다..."):
            try:
                # [Opal Step 2 & 3: Image Prompt 생성]
                img_p = (
                    f"Expert prompt for '{user_input}': "
                    "1. Replace animal parts with object components. "
                    "2. Apply thick, ultra-glossy, squishy Tanghulu-like glaze to all surfaces. "
                    "3. Photorealistic and surreal. IMPORTANT: Generate exactly one image."
                )
                img_res = model.generate_content(img_p).text

                # [Opal Step 4 & 5: Video Prompt 생성]
                vid_p = (
                    f"Video prompt
