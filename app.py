import streamlit as st
import google.generativeai as genai

# 1. 페이지 설정 (모바일/PC 최적화)
st.set_page_config(page_title="Bio-Mechanical Robot Factory", layout="centered")

# 2. API 및 모델 설정 (Secrets에서 키 불러오기)
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
    
    # 404 오류 방지를 위해 가장 안정적인 'gemini-1.5-flash' 모델 사용
    # 이 모델은 텍스트 생성 및 이미지 분석을 지원합니다.
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"⚠️ 설정 오류: {e}")
    st.info("Streamlit Secrets에 'GOOGLE_API_KEY'가 정확히 등록되었는지 확인해주세요.")

# 3. UI 디자인
st.markdown("<h1 style='text-align: center;'>🤖 Bio-Mechanical Robot Factory</h1>", unsafe_allow_html=True)
st.markdown("---")

user_input = st.text_input("로봇 재료 입력", placeholder="예: 딸기 고양이 로봇, 휴대폰 강아지 로봇...")

# 4. 프롬프트 생성 함수
def get_prompts(input_text):
    # 얼굴(인간 피부), 몸(금속), 내부 노출 및 탕후루 질감 지시
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
        
        with st.spinner("최첨단 로봇을 설계하고 이미지를 생성 중입니다..."):
            try:
                # [텍스트 및 설계 생성]
                response = model.generate_content(img_prompt)
                
                st.success("로봇 설계가 완료되었습니다!")
                
                # 결과 레이아웃 (2열 구성)
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("### 🖼️ Image Result")
                    # AI가 생성한 상세 설계 묘사 출력
                    st.write("**로봇 상세 설계:**")
                    st.write(response.text)
