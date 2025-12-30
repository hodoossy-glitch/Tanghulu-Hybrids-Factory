import streamlit as st
import google.generativeai as genai

# 1. 페이지 설정: 오팔 갤러리 스타일 (Surreal Elegance) 반영
st.set_page_config(page_title="Hybrid Creature Media Gallery", layout="wide")

# 스타일 설정: 다크 테마 및 카드 레이아웃 디자인
st.markdown("""
    <style>
    .main { background-color: #0b0e14; color: #ffffff; }
    h1 { font-family: 'Montserrat', sans-serif; text-align: center; color: #f0f0f0; margin-bottom: 30px; }
    .gallery-card { background: #161b22; padding: 25px; border-radius: 20px; border: 1px solid #30363d; margin-bottom: 20px; }
    .stButton>button { width: 100%; border-radius: 10px; background-color: #238636; color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 2. API 설정 및 모델 로드 (404 오류 해결 포인트)
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
    
    # 404 오류 방지를 위해 가장 보편적인 모델 식별자를 사용합니다.
    # models/ 접두사 없이 모델명만 입력하여 호환성을 높였습니다.
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"⚠️ 설정 오류: {e}")

# 3. 앱 헤더 및 입력 (Opal Step 1 반영)
st.markdown("<h1>✨ Hybrid Creature Media Gallery</h1>", unsafe_allow_html=True)
user_input = st.text_input("Describe your hybrid creature", placeholder="Violin Koala, Taxi Cat, Fridge Hippo...")

# 4. 실행 로직 (SyntaxError 및 404 완벽 해결)
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
