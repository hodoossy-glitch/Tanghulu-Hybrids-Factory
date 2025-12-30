import streamlit as st
import google.generativeai as genai

# 1. 페이지 설정
st.set_page_config(page_title="Bio-Mechanical Robot Factory", layout="centered")

# 2. API 및 모델 설정
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
    # 가장 안정적인 모델로 설정
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"⚠️ 설정 오류: {e}")

# 3. UI 디자인
st.markdown("<h1 style='text-align: center;'>🤖 Bio-Mechanical Robot Factory</h1>", unsafe_allow_html=True)
st.markdown("---")

user_input = st.text_input("로봇 재료 입력", placeholder="예: 딸기 고양이 로봇, 휴대폰 강아지 로봇...")

# 4. 프롬프트 생성 함수
def get_prompts(input_text):
    base_style = (
        "Face: Realistic human skin texture, expressive eyes. "
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
                # AI 모델 호출
                response = model.generate_content(img_prompt)
                
                st.success("로봇 설계가 완료되었습니다!")
                
                # 결과 레이아웃 (2열 구성)
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("### 🖼️ Image Result")
                    st.write("**로봇 상세 설계:**")
                    # response.text 출력 시 에러 방지 처리
                    if response.text:
                        st.write(response.text)
                    else:
                        st.write("설계 내용을 생성할 수 없습니다.")
                    
                    st.info("💡 위 설계를 바탕으로 시각화를 진행합니다.")
                    st.image("https://via.placeholder.com/512x512.png?text=Generating+Robot+Image...", use_container_width=True)

                with col2:
                    st.markdown("### 🎥 Video Result")
                    st.info("Veo 3.1을 통해 영상을 준비 중입니다.")
                    st.caption(f"Video Prompt: {vid_prompt}")

            except Exception as e:
                # try 블록 뒤에 반드시 필요한 except 블록
                st.error(f"생성 중 오류 발생: {e}")
