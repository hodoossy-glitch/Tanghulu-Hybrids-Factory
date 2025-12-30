import streamlit as st
import google.generativeai as genai

# 1. 페이지 설정: 오팔 미디어 페이지 가이드 (Surreal Elegance) 반영
st.set_page_config(page_title="Hybrid Creature Media Gallery", layout="wide")

# 2. 스타일링: 갤러리풍 다크 테마 및 반응형 레이아웃
st.markdown("""
    <style>
    .main { background-color: #0b0e14; color: #ffffff; }
    h1 { font-family: 'Montserrat', sans-serif; font-weight: 700; text-align: center; color: #f0f0f0; margin-bottom: 30px; }
    .gallery-card { background: #161b22; padding: 20px; border-radius: 15px; border: 1px solid #30363d; box-shadow: 0 8px 24px rgba(0,0,0,0.5); margin-bottom: 20px; }
    .stTextInput>div>div>input { background-color: #0d1117; color: white; border: 1px solid #30363d; border-radius: 10px; }
    .stButton>button { width: 100%; border-radius: 10px; background-color: #238636; color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. API 설정 (무료 키 사용)
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
    # 무료 등급에서 가장 빠르고 안정적인 모델 선택
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("⚠️ API 키 오류: Streamlit Secrets에 'GOOGLE_API_KEY'를 등록해주세요.")

# 4. 앱 헤더
st.markdown("<h1>✨ Hybrid Creature Media Gallery</h1>", unsafe_allow_html=True)

# 5. 사용자 입력 (Opal Step 1)
user_input = st.text_input("Describe your object-animal hybrid (e.g., 'Fridge Hippo')", placeholder="Violin Koala, Taxi Cat, Toaster Penguin...")

if st.button("🚀 Generate Artwork"):
    if user_input:
        with st.spinner("오팔 엔진이 초현실적 크리처를 설계 중입니다..."):
            try:
                # --- Opal Step 2 & 3: Image Prompt Engineering ---
                image_logic = f"""
                You are an expert image generation prompt engineer. Expand '{user_input}' into a visual prompt.
                1. Explicitly replace animal features with components of the object.
                2. Apply a thick, ultra-glossy, squishy Tanghulu-like glaze to all surfaces.
                3. Design for photorealistic, vibrant, and surreal appearance.
                IMPORTANT: Generate exactly one image.
                """
                img_res = model.generate_content(image_logic).text

                # --- Opal Step 4 & 5: Video Prompt Engineering ---
                video_logic = f"""
                Create a natural language prompt for a cinematic slow-motion video.
                1. Visual reference: {user_input} with thick Tanghulu glaze.
                2. Style: Cinematic slow-motion, no audio, less than 6 seconds.
                3. Effect: Vividly describe light reflections and squishy texture in motion.
                """
                vid_res = model.generate_content(video_logic).text

                # --- Opal Step 6: Gallery Rendering ---
                st.markdown(f"<h1>{user_input}</h1>", unsafe_allow_html=True)
                
                # 반응형 그리드 시스템 (PC: 2열, Mobile: 1열 자동 전환)
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown('<div class="gallery-card">', unsafe_allow_html=True)
                    st.markdown("### 🖼️ Hybrid Image Design")
                    st.write(img_res) # 오팔이 생성한 정교한 이미지 프롬프트 출력
                    st.image("https://via.placeholder.com/1024?text=Tanghulu+Glaze+Image+Concept", use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                with col2:
                    st.markdown('<div class="gallery-card">', unsafe_allow_html=True)
                    st.markdown("### 🎥 Cinematic Motion Design")
                    st.write(vid_res) # 오팔이 생성한 정교한 영상 프롬프트 출력
                    st.info("비디오 렌더링 준비 중: Cinematic slow-motion without audio.")
                    st.markdown('</div>', unsafe_allow_html=True)

                # 하단 추가 정보
                st.markdown("---")
                st.markdown("<h3 style='text-align: center;'>✋ 구독하기</h3>", unsafe_allow_html=True)
                st.write("<p style='text-align: center;'><b>딱-뉴스</b>를 구독하고 오팔 로직 기반의 최신 AI 앱 소스를 매일 확인하세요!</p>", unsafe_allow_html=True)

            except Exception as e:
                st.error(f"생성 중 오류 발생: {e}")
    else:
        st.warning("먼저 하이브리드 생명체의 이름을 입력해 주세요.")

# 푸터
st.markdown("<p style='text-align: center; color: #8b949e; font-size: 0.8rem;'>Created by DDAK-NEWS | Powered by Opal Logic & Gemini 1.5 Flash</p>", unsafe_allow_html=True)
