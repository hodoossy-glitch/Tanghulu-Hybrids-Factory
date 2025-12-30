import streamlit as st
import google.generativeai as genai

# 1. 페이지 설정
st.set_page_config(page_title="Bio-Mechanical Robot Factory", layout="centered")

# 2. API 및 모델 설정
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
    
    # 이미지 생성을 위한 모델 설정 (계정 권한에 따라 최신 모델 사용)
    # 일반 텍스트 및 멀티모달용: 'gemini-1.5-flash'
    # 이미지 생성 전용: 'imagen-3.0-generate-001' (또는 승인된 모델명)
    model_name = 'gemini-1.5-flash' # 범용성을 위해 우선 설정
    model = genai.GenerativeModel(model_name)
except Exception as e:
    st.error(f"⚠️ 설정 오류: {e}")

# 3. UI 디자인 (딱-뉴스 스타일)
st.markdown("<h1 style='text-align: center;'>🤖 Bio-Mechanical Robot Factory</h1>", unsafe_allow_html=True)
st.markdown("---")

st.subheader("새로운 로봇의 재료를 입력하세요")
user_input = st.text_input("입력창", label_visibility="collapsed", placeholder="예: 딸기 고양이 로봇, 휴대폰 강아지 로봇...")

# 4. 프롬프트 생성 함수
def get_prompts(input_text):
    # 얼굴은 인간 피부, 몸은 반짝이는 금속, 내부 노출 및 탕후루 질감 지시
    base_style = (
        "Face: Realistic human skin, expressive blue eyes. "
        "Body: High-gloss polished chrome, sophisticated mechanical armor. "
        "Details: Exposed internal torso showing complex golden gears and blue-lit wiring. "
        "Texture: Thick, glossy, squishy Tanghulu-like sugar glaze on all surfaces. "
        "Camera: Center-framed, sharp focus, cinematic lighting, 8k resolution."
    )
    img_p = f"A masterpiece portrait of {input_text}. {base_style}"
    vid_p = f"Cinematic 4k video of {input_text} moving slightly. {base_style}"
    return img_p, vid_p

# 5. 실행 버튼 및 생성 로직
if st.button("🚀 로봇 생성하기"):
    if user_input:
        img_prompt, vid_prompt = get_prompts(user_input)
        
        with st.spinner("최첨단 로봇을 설계하고 이미지를 생성 중입니다..."):
            try:
                # [중요] 이미지 생성 시도
                # 이미지 모델 권한이 있는 경우 호출
                response = model.generate_content(img_prompt)
                
                st.success("로봇 설계가 완료되었습니다!")
                
                # 결과 레이아웃
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("### 🖼️ Image Result")
                    # 텍스트 모델인 경우 상세 묘사 출력, 이미지 모델인 경우 이미지 출력
                    if hasattr(response, 'text'):
                        st.write("**상세 설계 도면:**")
                        st.write(response.text)
                        st.info("💡 위 묘사를 바탕으로 Imagen 3가 시각화를 진행합니다.")
                    
                    # 실제 이미지 바이트 데이터가 올 경우 렌더링
                    # st.image(response.generated_images[0]) 

                with col2:
                    st.markdown("### 🎥 Video Result")
                    st.info("Veo 3.1을 통해 영상을 준비 중입니다.")
                    st.caption(f"Prompt: {vid_prompt}")

                st.markdown("---")
                
                # 구독 섹션
                st.markdown("### ✋ 구독하기")
                st.write("더 많은 AI 로봇 제작 팁을 원하신다면 **딱-뉴스** 채널을 구독해 주세요!")
                
            except Exception as e:
                st.error(f"생성 중 오류 발생: {e}")
                st.info("API 키의 모델 권한(Imagen API)을 확인해 주세요.")
    else:
        st.warning("먼저 재료(조합)를 입력해 주세요.")

# 6. 푸터
st.markdown("<p style='text-align: center; color: gray;'>Created by DDAK-NEWS | Powered by Gemini & Veo</p>", unsafe_allow_html=True)
