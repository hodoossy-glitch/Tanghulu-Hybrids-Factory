import streamlit as st
import google.generativeai as genai

# 1. 페이지 설정
st.set_page_config(page_title="Bio-Mechanical Robot Factory", layout="centered")

# 2. API 키 및 모델 설정
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
    
    # 이미지 생성을 위해 지원되는 모델로 변경 (또는 일반 텍스트 모델 설정)
    # 현재 Imagen API는 별도의 권한이 필요할 수 있으므로, 
    # 기본적으로 텍스트/이미지 분석 모델인 gemini-1.5-flash를 테스트용으로 권장합니다.
    model = genai.GenerativeModel('gemini-1.5-flash') 
except Exception as e:
    st.error(f"⚠️ 설정 오류: {e}")

st.title("🤖 Bio-Mechanical Robot Factory")
st.markdown("---")

user_input = st.text_input("로봇 재료 입력", placeholder="예: 딸기 고양이 로봇...")

if st.button("🚀 로봇 생성하기"):
    if user_input:
        with st.spinner("로봇을 설계 중입니다..."):
            try:
                # 프롬프트 구성
                prompt = f"Detailed description for a robot: {user_input}. Face is human skin, body is polished chrome, internal gears visible, Tanghulu texture."
                
                # 모델 호출 (모델명 오류 해결을 위해 가장 범용적인 모델 사용)
                response = model.generate_content(prompt)
                
                st.success("설계가 완료되었습니다!")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("🖼️ Image Concept")
                    st.write(response.text) # 생성된 상세 설명 출력
                    # 실제 이미지 생성이 지원되는 계정인 경우 아래 코드 사용 가능
                    # st.image(response.generated_images[0])
                
                with col2:
                    st.subheader("🎥 Video Concept")
                    st.info("Veo 3.1 준비 중")

                st.markdown("---")
                st.markdown("### ✋ 구독하기")
                st.write("더 많은 AI 로봇 팁을 위해 **딱-뉴스**를 구독해 주세요!")

            except Exception as e:
                # 404 오류 발생 시 모델 리스트를 확인하도록 유도
                st.error(f"모델 호출 오류: {e}")
                st.info("Tip: API가 지원하는 모델 리스트는 genai.list_models()로 확인할 수 있습니다.")
