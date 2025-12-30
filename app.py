import streamlit as st
import google.generativeai as genai

# API 키 설정
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# ... (기존 UI 코드) ...

if st.button("🚀 로봇 생성하기"):
    if user_input:
        with st.spinner("이미지와 영상을 생성 중입니다..."):
            # 이미지 생성 호출 (예시 구조)
            model = genai.GenerativeModel('gemini-3-pro-image')
            response = model.generate_content(img_prompt)
            
            # 결과 표시
            st.image(response.generated_image) # 모델 응답에 따른 이미지 출력
