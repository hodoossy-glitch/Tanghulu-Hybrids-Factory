import streamlit as st
import google.generativeai as genai

# 1. 페이지 설정
st.set_page_config(page_title="Premium Bio-Robot Factory", layout="centered")

# 2. API 및 모델 설정
try:
    # Streamlit Secrets에 등록한 유료 계정 API 키를 가져옵니다.
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
    
    # Pro 결제 사용자라면 gemini-1.5-pro 모델을 안정적으로 사용할 수 있습니다.
    # 만약 여전히 404가 뜬다면 gemini-1.5-flash로 먼저 테스트해보세요.
    model = genai.GenerativeModel('gemini-1.5-pro')
except Exception as e:
    st.error(f"⚠️ 설정 오류: {e}")
    st.info("Secrets에 유료 계정의 API 키가 올바르게 입력되었는지 확인하세요.")

# 3. UI 디자인
st.markdown("<h1 style='text-align: center;'>🤖 Bio-Mechanical Robot Factory</h1>", unsafe_allow_html=True)
st.markdown("---")

user_input = st.text_input("로봇 재료 입력", placeholder="예: 딸기 고양이 로봇, 휴대폰 강아지 로봇...")

# 4. 프롬프트 생성 함수
def get_prompts(input_text):
    base_style = (
        "Face: Realistic human skin, expressive eyes. "
        "Body: High-gloss polished chrome, sophisticated mechanical armor. "
        "Details: Exposed internal torso showing complex golden gears and blue-lit wiring. "
        "Texture: Thick, glossy, squishy Tanghulu-like sugar glaze on all surfaces. "
        "Camera: Center-framed, sharp focus, cinematic lighting, 8k resolution."
    )
    img_p = f"A high-quality masterpiece portrait of {input_text}. {base_style}"
    vid_p = f"Cinematic 4k video of {input_text} moving slightly. {base_style}"
    return img_p, vid_p

# 5. 실행 버튼 및 생성 로직
if st.button("🚀 로봇 생성하기"):
    if user_input:
        img_prompt, vid_prompt = get_prompts(user_input)
        
        with st.spinner("최첨단 로봇을 설계 중입니다..."):
            try:
                # 유료 API 호출로 결과물 생성
                response = model.generate_content(img_prompt)
                
                st.success("로봇 설계가 완료되었습니다!")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("### 🖼️ Image Result")
                    if response and hasattr(response, 'text'):
                        st.write(response.text)
                    else:
                        st.write("결과를 불러오는 중입니다.")
                    st.image("https://via.placeholder.com/512x512.png?text=Premium+Robot+Image", use_container_width=True)

                with col2:
                    st.markdown("### 🎥 Video Result")
                    st.info("Veo 3.1 영상 생성 준비 중")
                    st.caption(f"Video Prompt: {vid_prompt}")

            except Exception as e:
                st.error(f"생성 중 오류 발생: {e}")
    else:
        # 이 else 문 뒤에 들여쓰기를 맞춰 warning을 배치했습니다.
        st.warning("먼저 재료(조합)를 입력해 주세요.")

# 6. 구독하기 및 푸터
st.markdown("---")
st.markdown("### ✋ 구독하기")
st.write("유료 API 활용 팁과 로봇 자동화 소식을 원하신다면 **딱-뉴스**를 구독하세요!")
st.markdown("<p style='text-align: center; color: gray;'>Created by DDAK-NEWS | Powered by Gemini Pro & Veo</p>", unsafe_allow_html=True)
