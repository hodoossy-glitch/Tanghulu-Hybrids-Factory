import streamlit as st
import google.generativeai as genai

# 1. 페이지 설정 (Opal Surreal Elegance 스타일)
st.set_page_config(page_title="Hybrid Creature Gallery", layout="wide")

# 스타일 설정: 갤러리풍 다크 테마 디자인
st.markdown("""
    <style>
    .main { background-color: #0b0e14; color: #ffffff; }
    h1 { font-family: 'Montserrat', sans-serif; text-align: center; color: #f0f0f0; }
    .gallery-card { background: #161b22; padding: 25px; border-radius: 20px; border: 1px solid #30363d; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 2. API 설정 및 모델 로드 (404 오류 방지)
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
    # 무료 등급에서 가장 안정적인 모델 경로를 사용합니다.
    model = genai.GenerativeModel('models/gemini-1.5-flash')
except Exception as e:
    st.error(f"설정 오류: {e}")

# 3. 입력 섹션 (Opal Step 1 반영)
st.markdown("<h1>✨ Hybrid Creature Media Gallery</h1>", unsafe_allow_html=True)
user_input = st.text_input("Describe your hybrid creature", placeholder="Violin Koala, Taxi Cat, Fridge Hippo...")

# 4. 실행 로직 (들여쓰기 및 SyntaxError 완벽 해결 버전)
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
                # SyntaxError 해결: try와 except 사이의 들여쓰기를 정확히 4칸으로 고정
                vid_p = (
                    f"Video prompt for {user_input}: "
                    "Cinematic slow-motion, 6 seconds, no audio. "
                    "Show thick Tanghulu-like glaze with vivid light reflections."
                )
                vid_res = model.generate_content(vid_p).text

                # [Opal Step 6: 갤러리 렌더링]
                st.markdown(f"<h1>{user_input}</h1>", unsafe_allow_html=True)
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown('<div class="gallery-card">', unsafe_allow_html=True)
                    st.write("### 🖼️ Hybrid Image Design")
                    st.write(img_res)
                    st.image("https://via.placeholder.com/1024?text=Tanghulu+Glaze+Rendering", use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                with col2:
                    st.markdown('<div class="gallery-card">', unsafe_allow_html=True)
                    st.write("### 🎥 Cinematic Motion Design")
                    st.write(vid_res)
                    st.info("비디오 렌더링 준비 중...")
                    st.markdown('</div>', unsafe_allow_html=True)

            except Exception as e:
                # 에러 해결의 핵심: try 블록과 수직 정렬이 완벽하게 맞는 위치
                st.error(f"생성 중 오류 발생: {e}")
    else:
        st.warning("먼저 내용을 입력해주세요.")

# 5. 하단 푸터 및 구독 섹션
st.markdown("---")
st.markdown("<h3 style='text-align: center;'>✋ 구독하기</h3>", unsafe_allow_html=True)
st.write("<p style='text-align: center;'><b>딱-뉴스</b>를 구독하고 에러 없는 오팔 전용 코드를 받아보세요!</p>", unsafe_allow_html=True)
