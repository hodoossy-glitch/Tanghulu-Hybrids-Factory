import streamlit as st
import google.generativeai as genai

# 1. 페이지 설정 및 디자인
st.set_page_config(page_title="Hybrid Creature Gallery", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0b0e14; color: #ffffff; }
    h1 { font-family: 'Montserrat', sans-serif; text-align: center; color: #f0f0f0; }
    .gallery-card { background: #161b22; padding: 25px; border-radius: 20px; border: 1px solid #30363d; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 2. API 설정
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('models/gemini-1.5-flash')
except Exception as e:
    st.error(f"설정 오류: {e}")

# 3. 입력 섹션 (Opal Step 1)
st.markdown("<h1>✨ Hybrid Creature Media Gallery</h1>", unsafe_allow_html=True)
user_input = st.text_input("Describe your hybrid", placeholder="Violin Koala, Taxi Cat...")

# 4. 생성 로직 (들여쓰기 오류 해결 버전)
if st.button("🚀 Generate Artwork"):
    if user_input:
        with st.spinner("설계 중..."):
            try:
                # [Opal Step 2 & 3: Image Prompt]
                img_p = (
                    f"Expert prompt for '{user_input}': "
                    "Replace animal parts with object parts. "
                    "Apply thick, ultra-glossy, squishy Tanghulu glaze to all surfaces. "
                    "Photorealistic, surreal. IMPORTANT: Generate exactly one image."
                )
                img_res = model.generate_content(img_p).text

                # [Opal Step 4 & 5: Video Prompt]
                vid_p = (
                    f"Video prompt for {user_input}: "
                    "Cinematic slow-motion, 6s, no audio. "
                    "Show thick Tanghulu glaze with vivid light reflections."
                )
                vid_res = model.generate_content(vid_p).text

                # [Opal Step 6: Render Page]
                st.markdown(f"<h1>{user_input}</h1>", unsafe_allow_html=True)
                c1, c2 = st.columns(2)
                
                with c1:
                    st.markdown('<div class="gallery-card">', unsafe_allow_html=True)
                    st.write("### 🖼️ Image Design")
                    st.write(img_res)
                    st.image("https://via.placeholder.com/1024?text=Tanghulu+Rendering", use_container
