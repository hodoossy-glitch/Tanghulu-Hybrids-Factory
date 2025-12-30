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

# 2. API 설정 (갱신된 무료 키 사용)
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
    # 무료 등급 최적화 모델
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("⚠️ API 키를 갱신하고 Streamlit Secrets에 등록해주세요.")

# 3. 앱 헤더 및 입력 (Opal Step 1)
st.markdown("<h1>✨ Hybrid Creature Media Gallery</h1>", unsafe_allow_html=True)
user_input = st.text_input("Describe your hybrid (e.g., 'Fridge Hippo')", placeholder="Violin Koala, Taxi Cat...")

if st.button("🚀 Generate Artwork"):
    if user_input:
        with st.spinner("오팔 엔진이 크리처를 설계 중입니다..."):
            try:
                # [Opal Step 2 & 3: Image Prompt Logic]
                img_logic = f"""
                You are an expert prompt engineer. Expand '{user_input}' into a visual prompt.
                1. Detail how animal features are replaced by object parts.
                2. Apply a thick, ultra-glossy, squishy Tanghulu-like glaze to all surfaces.
                3. High-quality, photorealistic, surreal appearance.
                IMPORTANT: Generate exactly one image.
                """
                img_res = model.generate_content(img_logic).text

                # [Opal Step 4 & 5: Video Prompt Logic]
                vid_logic = f"""
                Create a natural language prompt for a 6s cinematic slow-motion video.
                1. Content: {user_input} with thick Tanghulu-like glaze.
                2. Movement: Impactful slow-motion action with light reflections on glossy surface.
                3. Style: No audio, cinematic elegance.
                """
                vid_res = model.generate_content(vid_logic).text

                # [Opal Step 6: Gallery Rendering]
                st.markdown(f"<h1>{user_input}</h1>", unsafe_allow_html=True)
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown('<div class="gallery-card">', unsafe_allow_html=True)
                    st.markdown("### 🖼️ Hybrid Image Design")
                    st.write(img_res) # 오팔 상세 프롬프트 출력
                    st.image("https://via.placeholder.com/1024?text=Tanghulu+Glaze+Rendering...", use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                with col2:
                    st.markdown('<div class="gallery-card">', unsafe_allow_html=True)
                    st.markdown("### 🎥 Cinematic Motion Design")
                    st.write(vid_res) # 오팔 영상 프롬프트 출력
                    st.info("비디오 렌더링 준비 중: Cinematic slow-motion without audio.")
                    st.markdown('</div>', unsafe_allow_html=True)

            except Exception as e:
                st.error(f"생성 중 오류 발생: {e}")
    else:
        st.warning("내용을 입력해주세요.")

# 하단 구독 섹션
st.markdown("---")
st.markdown("<h3 style='text-align: center;'>✋ 구독하기</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'><b>딱-뉴스</b>를 구독하고 매일 새로운 AI 로봇 앱 소스를 받아보세요!</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Created by DDAK-NEWS | Powered by Opal Logic & Gemini 1.5 Flash</p>", unsafe_allow_html=True)
