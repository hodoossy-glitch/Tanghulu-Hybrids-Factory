import streamlit as st
import google.generativeai as genai

# 1. 페이지 설정 (유지)
st.set_page_config(page_title="Hybrid Creature Gallery", layout="wide")

# 스타일 설정 (유지)
st.markdown("""
    <style>
    .main { background-color: #0b0e14; color: #ffffff; }
    h1 { font-family: 'Montserrat', sans-serif; text-align: center; color: #f0f0f0; }
    .gallery-card { background: #161b22; padding: 25px; border-radius: 20px; border: 1px solid #30363d; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 2. API 설정 (404 오류 수정)
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
    # 모델 경로명을 명확히 지정하여 404 오류를 방지합니다.
    model = genai.GenerativeModel('models/gemini-1.5-flash')
except Exception as e:
    st.error(f"⚠️ 설정 오류: {e}")

# 3. 앱 헤더 및 입력 (유지)
st.markdown("<h1>✨ Hybrid Creature Media Gallery</h1>", unsafe_allow_html=True)
user_input = st.text_input("Describe your hybrid (e.g., 'Fridge Hippo')", placeholder="Violin Koala, Taxi Cat...")

# 4. 실행 로직 (SyntaxError 수정)
if st.button("🚀 Generate Artwork"):
    if user_input:
        with st.spinner("오팔 엔진이 크리처를 설계 중입니다..."):
            try:
                # [Opal Step 2 & 3: 문자열 끊김 방지를 위해 괄호로 처리]
                img_logic = (
                    f"You are an expert prompt engineer. Expand '{user_input}' into a detailed visual prompt. "
                    "1. Explicitly describe how the animal's features are replaced by components of the object. "
                    "2. Apply a thick, ultra-glossy, squishy Tanghulu-like glaze to all surfaces. "
                    "3. High-quality, photorealistic, vibrant, and surreal appearance. "
                    "IMPORTANT: Generate exactly one image."
                )
                img_res = model.generate_content(img_logic).text

                # [Opal Step 4 & 5: SyntaxError 발생 지점 수정]
                vid_logic = (
                    f"Create a natural language prompt for a cinematic slow-motion video of {user_input}. "
                    "1. Apply a thick, ultra-glossy, squishy Tanghulu-like glaze throughout. "
                    "2. Motion: Impactful slow-motion action with light reflections. "
                    "3. Duration: Less than 6 seconds, no audio."
                )
                vid_res = model.generate_content(vid_logic).text

                # [Opal Step 6: 갤러리 렌더링 유지]
                st.markdown(f"<h1>{user_input}</h1>", unsafe_allow_html=True)
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown('<div class="gallery-card">', unsafe_allow_html=True)
                    st.markdown("### 🖼️ Hybrid Image Design")
                    st.write(img_res)
                    st.image("https://via.placeholder.com/1024?text=Tanghulu+Glaze+Rendering...", use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                with col2:
                    st.markdown('<div class="gallery-card">', unsafe_allow_html=True)
                    st.markdown("### 🎥 Cinematic Motion Design")
                    st.write(vid_res)
                    st.info("비디오 렌더링 준비 중: Cinematic slow-motion without audio.")
                    st.markdown('</div>', unsafe_allow_html=True)

            except Exception as e:
                st.error(f"생성 중 오류 발생: {e}")
    else:
        st.warning("내용을 입력해주세요.")

# 푸터 (유지)
st.markdown("---")
st.markdown("<h3 style='text-align: center;'>✋ 구독하기</h3>", unsafe_allow_html=True)
st.write("<p style='text-align: center;'><b>딱-뉴스</b>를 구독하고 오팔 로직 기반의 최신 AI 앱 소스를 받아보세요!</p>", unsafe_allow_html=True)
