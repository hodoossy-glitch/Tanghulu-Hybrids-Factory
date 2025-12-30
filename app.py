import streamlit as st
import google.generativeai as genai

# --------------------------------------------------
# 1. 페이지 설정
# --------------------------------------------------
st.set_page_config(
    page_title="Hybrid Creature Media Gallery",
    layout="wide"
)

# --------------------------------------------------
# 2. 스타일 (다크 갤러리 테마)
# --------------------------------------------------
st.markdown("""
<style>
.main { background-color: #0b0e14; color: #ffffff; }
h1 { text-align: center; color: #f0f0f0; margin-bottom: 30px; }
.gallery-card {
    background: #161b22;
    padding: 25px;
    border-radius: 20px;
    border: 1px solid #30363d;
    margin-bottom: 20px;
}
.stButton>button {
    width: 100%;
    border-radius: 10px;
    background-color: #238636;
    color: white;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# 3. API 설정 (에러 방지)
# --------------------------------------------------
API_KEY = st.secrets.get("GOOGLE_API_KEY")
if not API_KEY:
    st.error("⚠️ GOOGLE_API_KEY가 설정되지 않았습니다.")
    st.stop()

genai.configure(api_key=API_KEY)

try:
    model = genai.GenerativeModel("gemini-1.5-flash")
except Exception as e:
    st.error(f"모델 로드 실패: {e}")
    st.stop()

# --------------------------------------------------
# 4. 헤더 & 입력
# --------------------------------------------------
st.markdown("<h1>✨ Hybrid Creature Media Gallery</h1>", unsafe_allow_html=True)

user_input = st.text_input(
    "Describe your hybrid creature",
    placeholder="Fridge Hippo, Taxi Cat, Violin Koala..."
)

# --------------------------------------------------
# 5. 실행 로직
# --------------------------------------------------
if st.button("🚀 Generate Artwork"):
    if not user_input:
        st.warning("먼저 하이브리드 설명을 입력해주세요.")
    else:
        with st.spinner("Gemini가 프롬프트를 생성 중입니다..."):
            try:
                # 이미지 프롬프트 (텍스트 생성)
                image_prompt = f"""
You are an expert image generation prompt engineer.

Create a highly detailed, photorealistic image prompt for a hybrid creature described as:
"{user_input}"

Replace the animal's anatomical features with components of the object.
Apply a thick, ultra-glossy, squishy Tanghulu-like glaze to all surfaces.
The glaze should appear translucent, candy-coated, reflective, and slightly bulging.

Use cinematic lighting, realistic shadows, depth of field, and premium material textures.
Clean or cinematic background.

IMPORTANT: Generate exactly one image.
""".strip()

                image_result = model.generate_content(image_prompt).text

                # 비디오 프롬프트 (텍스트 생성)
                video_prompt = f"""
Create a cinematic video generation prompt for:
"{user_input}"

6 seconds duration, slow motion.
Focus on light reflections over thick Tanghulu-like glaze.
No audio. Premium cinematic mood.
""".strip()

                video_result = model.generate_content(video_prompt).text

                # --------------------------------------------------
                # 6. 갤러리 출력
                # --------------------------------------------------
                st.markdown(f"<h1>{user_input}</h1>", unsafe_allow_html=True)

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown('<div class="gallery-card">', unsafe_allow_html=True)
                    st.markdown("### 🖼️ Image Generation Prompt")
                    st.write(image_result)
                    st.image(
                        "https://via.placeholder.com/1024x1024?text=Image+Generated+Externally"
                    )
                    st.markdown('</div>', unsafe_allow_html=True)

                with col2:
                    st.markdown('<div class="gallery-card">', unsafe_allow_html=True)
                    st.markdown("### 🎥 Video Generation Prompt")
                    st.write(video_result)
                    st.info("비디오는 외부 모델(Veo, Runway 등)에서 생성하세요.")
                    st.markdown('</div>', unsafe_allow_html=True)

            except Exception as e:
                st.error(f"생성 중 오류 발생: {e}")

# --------------------------------------------------
# 7. 푸터
# --------------------------------------------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#888;'>Hybrid Creature Prompt Gallery · Powered by Gemini</p>",
    unsafe_allow_html=True
)
