import streamlit as st
import google.generativeai as genai

# 1. 페이지 설정 및 디자인
st.set_page_config(page_title="Bio-Robot Factory", layout="centered")

# 2. API 설정 (무료 키 사용)
try:
    # Streamlit Secrets에 등록된 무료 API 키를 가져옵니다.
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
    # 가장 범용적이고 빠른 gemini-1.5-flash 모델을 사용합니다.
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"⚠️ 설정 오류: {e}")
    st.info("Secrets에 API 키가 정확히 등록되었는지 확인해주세요.")

# 3. UI 디자인 (딱-뉴스 스타일)
st.markdown("<h1 style='text-align: center;'>🤖 Bio-Mechanical Robot Factory</h1>", unsafe_allow_html=True)
st.markdown("---")

st.subheader("새로운 로봇의 재료를 입력하세요")
user_input = st.text_input("로봇 조합 입력", placeholder="예: 딸기 고양이 로봇, 바이올린 표범...")

# 4. 프롬프트 생성 로직 (사물-동물 결합 + 탕후루 질감)
def generate_robot_design(input_text):
    design_prompt = (
        f"Generate a detailed visual description for a hybrid creature: '{input_text}'. "
        "Rule 1: The face must have flawless, realistic human skin with gentle eyes. "
        "Rule 2: The body must be made of high-gloss polished chrome and mechanical parts from the object. "
        "Rule 3: Show intricate internal gears and blue-lit wiring through an exposed torso. "
        "Rule 4: Apply a mandatory 'glossy, squishy, Tanghulu-like glaze' to all surfaces. "
        "Rule 5: Professional 8k macro photography style, center-framed."
    )
    return design_prompt

# 5. 실행 버튼 및 결과 출력
if st.button("🚀 로봇 설계 시작하기"):
    if user_input:
        with st.spinner("AI 유전 공학자가 로봇을 설계 중입니다..."):
            try:
                # 설계 지침 생성
                base_design = generate_robot_design(user_input)
                # AI 모델이 상세 묘사 생성
                response = model.generate_content(base_design)
                
                st.success("로봇 설계 도면이 완성되었습니다!")
                
                # 결과 레이아웃 (프롬프트 집중형)
                st.markdown("### 🖼️ Image Generation Prompt")
                st.info("이 프롬프트를 복사하여 Imagen 3나 미드저니에 사용하세요.")
                st.code(response.text if response.text else "설계안을 생성할 수 없습니다.")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("#### ✨ 핵심 특징")
                    st.write("- 탕후루 광택 코팅")
                    st.write("- 인간 피부 얼굴")
                    st.write("- 기계식 내부 기어")
                
                with col2:
