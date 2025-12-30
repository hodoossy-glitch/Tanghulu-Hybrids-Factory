import streamlit as st
import google.generativeai as genai

# 1. 페이지 설정: 오팔 미디어 페이지 스타일 (Surreal Elegance)
st.set_page_config(page_title="Hybrid Creature Gallery", layout="wide")

# 스타일 설정: 갤러리풍 다크 테마
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
    # 404 오류 방지를 위해 표준 모델명을 사용합니다.
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"⚠️ 설정 오류: {e}")

# 3. 앱 헤더 및 입력 (Opal Step 1)
st.markdown("<h1>✨ Hybrid Creature Media Gallery</h1>", unsafe_allow_html=True)
user_input = st.text_input("Describe your hybrid (e.g., 'Fridge Hippo')", placeholder="Violin Koala, Taxi Cat...")

# 4. 실행 버튼 및 생성 로직
if st.button("🚀 Generate Artwork"):
    if user_input:
        with st.spinner("오팔 엔진이 크리처를 설계 중입니다..."):
            try:
                # [Opal Step 2 & 3: Image Prompt Logic]
                img_logic = (
                    f"You are an expert prompt engineer. Expand '{user_input}' into a detailed visual prompt. "
                    "1. Explicitly describe how the animal's features are replaced by components of the object. "
                    "2. Apply a thick, ultra-glossy, squishy Tanghulu-like glaze to all surfaces. "
                    "3. High-quality, photorealistic, vibrant, and surreal appearance. "
                    "IMPORTANT: Generate exactly one image."
                )
                response_img = model.generate_content(img_logic)
                img_res = response_img.text

                #
