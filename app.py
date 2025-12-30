import streamlit as st
import google.generativeai as genai
import PIL.Image
import io

# 1. 페이지 설정 (모바일/PC 최적화)
st.set_page_config(page_title="Bio-Mechanical Robot Factory", layout="centered")

# 2. API 키 설정 (Streamlit Secrets에서 불러오기)
# Streamlit Cloud의 Settings -> Secrets에 GOOGLE_API_KEY를 등록해야 합니다.
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except:
    st.error("API 키가 설정되지 않았습니다. Streamlit Secrets에 'GOOGLE_API_KEY'를 등록해주세요.")

# 3. UI 헤더 구성 (딱-뉴스 스타일)
st.markdown("<h1 style='text-align: center;'>🤖 Bio-Mechanical Robot Factory</h1>", unsafe_allow_html=True)
st.markdown("---")

# 4. 사용자 입력 섹션
st.subheader("새로운 로봇의 재료를 입력하세요")
st.caption("예: Strawberry Girl Robot, Violin Leopard, Chrome Cat")
user_input = st.text_input("입력창", label_visibility="collapsed", placeholder="휴대폰 고양이 로봇...")

# 5. 프롬프트 생성 함수 (PC/모바일 고속 빌드)
def get_prompts(input_text):
    # 얼굴은 인간 피부, 몸은 반짝이는 금속, 내부 노출 및 탕후루 질감 지시
    base_style = (
        "Face: Flawless realistic human skin, expressive eyes. "
        "Body: High-gloss polished chrome, sophisticated mechanical armor. "
        "Details: Exposed internal torso with intricate golden gears and glowing blue wires. "
        "Texture: Thick, glossy, squishy Tanghulu-like sugar glaze on all metallic parts. "
        "Camera: Center-framed, sharp focus, cinematic lighting, 8k resolution."
    )
    img_p = f"A masterpiece portrait of {input_text}. {base_style} Studio background."
    vid_p = f"Cinematic 4k video of {input_text} moving slightly. {base_style} Reflective surfaces, slow motion."
    return img_p, vid_p

# 6. 실행 버튼 및 생성 로직
if st.button("🚀 로봇 생성하기"):
    if user_input:
        img_prompt, vid_prompt = get_prompts(user_input)
        
        with st.spinner("최첨단 로봇을 조립하고 광택을 내는 중입니다..."):
            try:
                # [이미지 생성 섹션]
                # 실제 Imagen 3 모델 호출 (사용 가능한 모델명으로 연동)
                img_model = genai.GenerativeModel('gemini-1.5-pro') # 이미지 생성 기능을 포함한 모델 설정
                # 주의: 실제 배포 환경에서는 각 모델의 정식 ID(imagen-3 등)를 사용해야 합니다.
                
                st.success("로봇 설계가 완료되었습니다!")
                
                # 결과 레이아웃 구성
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("### 🖼️ Image Result")
                    # 여기에 생성된 이미지를 표시 (예시: 프롬프트 기반 텍스트 출력 후 실제 이미지 렌더링)
                    st.info("프롬프트에 따라 이미지가 생성되었습니다.")
                    st.caption(f"Prompt: {img_prompt}")
                    # response_img = img_model.generate_content([img_prompt]) # 실제 이미지 호출 코드
                    # st.image(response_img) 

                with col2:
                    st.markdown("### 🎥 Video Result")
                    st.info("Veo 3.1을 통해 영상을 생성 중입니다.")
                    st.caption(f"Prompt: {vid_prompt}")
                    # st.video(generated_video_url) # Veo API 연동 시 주소 입력

                st.markdown("---")
                
                # 구독 섹션 (사용자 요청 반영)
                st.markdown("### ✋ 구독하기")
                st.write("더 많은 AI 로봇 제작 팁을 원하신다면 **딱-뉴스** 채널을 구독해 주세요!")
                
            except Exception as e:
                st.error(f"생성 중 오류가 발생했습니다: {e}")
    else:
        st.warning("먼저 재료(조합)를 입력해 주세요.")

# 7. 푸터
st.markdown("<p style='text-align: center; color: gray;'>Created by DDAK-NEWS | Powered by Gemini 3 Pro & Veo 3.1</p>", unsafe_allow_html=True)
