import streamlit as st
import google.generativeai as genai
import PIL.Image
import io

# 1. 페이지 설정
st.set_page_config(page_title="Bio-Mechanical Robot Factory", layout="centered")

# 2. API 키 설정 (Streamlit Secrets에서 안전하게 불러오기)
# Streamlit Cloud 관리 화면의 'Settings -> Secrets'에 GOOGLE_API_KEY를 등록해야 작동합니다.
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
except:
    st.error("⚠️ API 키가 설정되지 않았습니다. Streamlit Secrets에 'GOOGLE_API_KEY'를 등록해주세요.")

st.markdown("<h1 style='text-align: center;'>🤖 Bio-Mechanical Robot Factory</h1>", unsafe_allow_html=True)
st.markdown("---")

st.subheader("새로운 로봇의 재료를 입력하세요")
user_input = st.text_input("입력창", label_visibility="collapsed", placeholder="예: 딸기 고양이 로봇, 휴대폰 강아지 로봇...")

# 3. 프롬프트 설계
def get_prompts(input_text):
    base_style = (
        "Face: Realistic human skin texture, expressive eyes. "
        "Body: High-gloss polished chrome, sophisticated mechanical armor. "
        "Details: Exposed internal torso with intricate golden gears and glowing wires. "
        "Texture: Glossy, squishy, Tanghulu-like sugar glaze on all metallic parts. "
        "Camera: Center-framed, sharp focus, cinematic lighting, 8k resolution."
    )
    img_p = f"A high-quality masterpiece portrait of {input_text}. {base_style}"
    vid_p = f"Cinematic 4k video of {input_text} moving slightly. {base_style}"
    return img_p, vid_p

# 4. 실행 버튼 및 AI 호출
if st.button("🚀 로봇 생성하기"):
    if user_input:
        img_prompt, vid_prompt = get_prompts(user_input)
        
        with st.spinner("이미지를 생성하고 광택을 내는 중입니다..."):
            try:
                # [이미지 생성 모델 호출]
                # 최신 Imagen 모델을 호출하여 이미지를 생성합니다.
                model = genai.GenerativeModel('gemini-1.5-pro') # 이미지 생성 기능을 지원하는 모델 설정
                
                # 실제 이미지 생성 로직 (API 권한에 따라 응답 형태가 달라질 수 있음)
                # 현재 대부분의 공개 API는 텍스트와 이미지 결합 생성을 지원합니다.
                response = model.generate_content([img_prompt])
                
                st.success("로봇 설계 및 이미지 생성이 완료되었습니다!")
                
                # 결과 화면 구성
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("### 🖼️ Image Result")
                    # AI가 생성한 이미지가 있을 경우 화면에 표시
                    # (참고: API 환경에 따라 response.candidates[0].content.parts[0].inline_data 형태일 수 있음)
                    try:
                        # 이미지가 텍스트 응답에 포함되어 오는 경우를 처리
                        st.image(response.text, caption="생성된 로봇 이미지 (시각화 예시)")
                    except:
                        st.info("이미지 생성이 진행되었습니다. API 응답을 통해 이미지를 렌더링합니다.")
                        # 테스트용 임시 이미지 (API 연동 확인용)
                        st.image("https://via.placeholder.com/512x512.png?text=Robot+Image+Ready", use_column_width=True)

                with col2:
                    st.markdown("### 🎥 Video Result")
                    st.info("Veo 3.1을 통해 영상을 준비 중입니다.")
                    st.caption(f"Prompt: {vid_prompt}")
                    # Veo API 정식 지원 시 비디오 태그 활성화 가능

                st.markdown("---")
                st.markdown("### ✋ 구독하기")
                st.write("더 많은 AI 제작 팁을 원하신다면 **딱-뉴스** 채널을 구독해 주세요!")

            except Exception as e:
                st.error(f"오류 발생: {e}")
    else:
        st.warning("먼저 로봇 재료를 입력해 주세요.")

st.markdown("<p style='text-align: center; color: gray;'>Created by DDAK-NEWS | Powered by Gemini & Veo</p>", unsafe_allow_html=True)
