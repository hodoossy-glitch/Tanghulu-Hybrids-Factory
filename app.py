import streamlit as st
import google.generativeai as genai
import time

# 1. 페이지 설정 및 디자인
st.set_page_config(page_title="Bio-Robot Factory", layout="centered")
st.title("🤖 Bio-Mechanical Robot Factory")
st.markdown("---")

# 2. 사용자 입력 섹션
st.subheader("새로운 로봇의 재료를 입력하세요")
user_input = st.text_input("예: Strawberry Girl Robot, Violin Leopard, Chrome Cat", placeholder="조합을 입력하세요...")

# 3. AI 로직 (Single-pass mapping)
def generate_robot_content(input_text):
    # PC 및 모바일 속도 최적화를 위한 핵심 프롬프트 설계
    core_style = (
        "Face: Realistic human skin texture, blue eyes, gentle expression. "
        "Body: High-gloss polished chrome and sophisticated mechanical parts. "
        "Internals: Exposed torso showing complex golden gears and blue-lit wiring. "
        "Texture: Mandatory 'glossy, squishy, Tanghulu-like glaze' on all mechanical surfaces. "
        "Environment: Cinematic lighting, 8k, center-framed, blurred park background."
    )
    
    image_prompt = f"A hyper-detailed portrait of a {input_text}. {core_style}"
    video_prompt = f"Cinematic 4k video of a {input_text}. The robot moves smoothly, reflecting light off its glossy body. {core_style}"
    
    return image_prompt, video_prompt

# 4. 생성 버튼 및 실행
if st.button("🚀 로봇 생성하기"):
    if user_input:
        with st.spinner("최첨단 로봇을 조립 중입니다. 잠시만 기다려 주세요..."):
            img_prompt, vid_prompt = generate_robot_content(user_input)
            
            # 실제 모델 호출 부분 (여기서는 프롬프트 출력 시뮬레이션)
            # 실제 사용 시 st.secrets["GOOGLE_API_KEY"] 등으로 인증 필요
            time.sleep(2) # 처리 대기 시간 시뮬레이션
            
            st.success("로봇 설계가 완료되었습니다!")
            
            # 결과 표시 레이아웃
            col1, col2 = st.columns(2)
            with col1:
                st.info("🖼️ Image Prompt")
                st.code(img_prompt)
                # st.image(generated_image_url) # 실제 이미지 API 연결 시
            
            with col2:
                st.info("🎥 Video Prompt")
                st.code(vid_prompt)
                # st.video(generated_video_url) # 실제 비디오 API 연결 시
                
            st.markdown("---")
            st.markdown("### ✋ 구독하기")
            st.write("더 많은 AI 로봇 제작 팁을 원하신다면 채널을 구독해 주세요!")
    else:
        st.warning("먼저 재료(조합)를 입력해 주세요.")

# 푸터 (Footer)
st.markdown("Created by **DDAK-NEWS** | Powered by Gemini 3 Pro & Veo 3.1")
