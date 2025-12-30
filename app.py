import streamlit as st
import google.generativeai as genai

# 1. 페이지 설정: 오팔 미디어 페이지 스타일 (Surreal Elegance)
st.set_page_config(page_title="Hybrid Creature Gallery", layout="wide")

# 2. 스타일링: 갤러리풍 다크 테마 적용
st.markdown("""
    <style>
    .main { background-color: #121212; color: #ffffff; }
    h1 { font-family: 'Poppins', sans-serif; font-weight: 600; text-align: center; color: #E0E0E0; margin-bottom: 50px; }
    .card { background: #1E1E1E; padding: 20px; border-radius: 15px; border: 1px solid #333; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }
    footer { text-align: center; color: #555; font-size: 0.8rem; margin-top: 50px; }
    </style>
    """, unsafe_allow_html=True)

# 3. API 설정
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
    # 유료 등급은 gemini-1.5-pro, 무료는 gemini-1.5-flash 권장
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("API 키 설정 오류가 발생했습니다.")

# 4. 사용자 입력 (Opal Step 1)
st.markdown("<h1>✨ Hybrid Creature Media Gallery</h1>", unsafe_allow_html=True)
user_input = st.text_input("Describe your object-animal hybrid (e.g., 'Fridge Hippo')", placeholder="Fridge Hippo, Taxi Cat, Violin Koala...")

if st.button("🚀 Generate Artwork"):
    if user_input:
        with st.spinner("AI가 초현실적 생명체를 설계하고 갤러리를 준비 중입니다..."):
            try:
                # --- Step 2 & 3: Generate Image Prompt (Opal Logic) ---
                image_prompt_base = f"""
                You are an expert image generation prompt engineer. Expand '{user_input}' into a detailed prompt.
                1. Describe how animal features are replaced by components of the object.
                2. Apply a thick, ultra-glossy, squishy Tanghulu-like glaze to all surfaces.
                3. High-quality, photorealistic, vibrant, and surreal appearance.
                IMPORTANT: Generate exactly one image.
                """
                # AI를 통해 오팔 수준의 정교한 프롬프트 생성
                img_prompt_res = model.generate_content(image_prompt_base).text

                # --- Step 4 & 5: Generate Video Prompt (Opal Logic) ---
                video_prompt_base = f"""
                Create a natural language prompt for a 6-second slow-motion video.
                1. Base: {user_input} with Tanghulu-like glaze.
                2. Style: Cinematic slow-motion, no audio.
                3. Focus: Light reflections on the squishy, glossy surface and impactful brief action.
                """
                vid_prompt_res = model.generate_content(video_prompt_base).text

                # 5. 결과 레이아웃 (Opal Step 6: Render Media Page)
                st.markdown(f"<h1>{user_input}</h1>", unsafe_allow_html=True)
                
                # 가로 배치를 위한 컬럼 (Large screen side-by-side, Small screen stack)
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown('<div class="card">', unsafe_allow_html=True)
                    st.markdown("### 🖼️ Hybrid Image")
                    # 실제 Imagen 3 호출을 대신하는 상세 설계안 출력 및 이미지 영역
                    st.write(img_prompt_res)
                    st.image("https://via.placeholder.com/1024x1024.png?text=Generating+Glossy+Creature...", use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                with col2:
                    st.markdown('<div class="card">', unsafe_allow_html=True)
                    st.markdown("### 🎥 Cinematic Video")
                    # 실제 Veo 3.1 호출을 대신하는 영상 설계안 출력
                    st.write(vid_prompt_res)
                    st.info("Autoplay cinematic video is being rendered...")
                    st.markdown('</div>', unsafe_allow_html=True)

                # 하단 추가 정보
                st.markdown("---")
                st.markdown("### ✋ 구독하기")
                st.write("**딱-뉴스** 채널을 구독하시면 오팔(Opal)의 고급 로직을 활용한 더 많은 앱 소스를 확인하실 수 있습니다!")

            except Exception as e:
                st.error(f"생성 중 오류 발생: {e}")
    else:
        st.warning("먼저 생명체의 이름을 입력해 주세요.")

# 푸터
st.markdown("<footer>Created by DDAK-NEWS | Powered by Opal Logic & Gemini</footer>", unsafe_allow_html=True)
