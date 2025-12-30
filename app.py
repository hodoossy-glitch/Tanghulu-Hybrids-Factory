import streamlit as st

# --------------------------------------------------
# 1. 페이지 설정
# --------------------------------------------------
st.set_page_config(
    page_title="Hybrid Creature Prompt Generator",
    page_icon="🧬",
    layout="centered"
)

# --------------------------------------------------
# 2. 간단한 스타일
# --------------------------------------------------
st.markdown("""
<style>
.main { background-color: #0b0e14; color: #ffffff; }
h1 { text-align: center; margin-bottom: 30px; }
.stButton>button {
    width: 100%;
    border-radius: 10px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# 3. 헤더
# --------------------------------------------------
st.markdown("<h1>🧬 Hybrid Creature Image Prompt Generator</h1>", unsafe_allow_html=True)
st.write(
    "오브젝트 + 동물 하이브리드를 입력하면\n"
    "**Tanghulu 글레이즈 이미지 생성 프롬프트**를 만들어줍니다."
)

# --------------------------------------------------
# 4. 사용자 입력
# --------------------------------------------------
hybrid_description = st.text_input(
    "Hybrid Creature Description",
    placeholder="Fridge Hippo, Taxi Cat, Violin Koala..."
)

# --------------------------------------------------
# 5. 프롬프트 생성
# --------------------------------------------------
if st.button("🚀 Generate Prompt"):
    if not hybrid_description:
        st.warning("하이브리드 설명을 입력하세요.")
    else:
        image_generation_prompt = f"""
You are an expert image generation prompt engineer, specializing in hyper-detailed, photorealistic visuals.

Create a single, high-quality image of a hybrid creature described as:
"{hybrid_description}"

The creature should combine an animal and an object.
Clearly replace the animal’s anatomical features with components of the object
(e.g., fur replaced by metal panels, eyes replaced by LED screens, limbs formed from object parts).

All surfaces of the creature must be coated in a thick, ultra-glossy, squishy Tanghulu-like glaze.
The glaze should appear translucent, candy-coated, reflective, slightly bulging, and sticky,
as if the creature was dipped in hardened sugar syrup.

Use cinematic lighting, realistic shadows, depth of field, and photorealistic material textures.
The creature should feel physically real despite its surreal design.
Use a clean or cinematic background that does not distract from the subject.

IMPORTANT: Generate exactly one image.
""".strip()

        st.subheader("📸 Image Generation Prompt")
        st.text_area(
            label="Copy & paste this prompt into Opal / Imagen / DALL·E",
            value=image_generation_prompt,
            height=420
        )

        st.success("프롬프트 생성 완료! 🎉")

# --------------------------------------------------
# 6. 푸터
# --------------------------------------------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#888;'>Prompt-only version · No API · No Errors</p>",
    unsafe_allow_html=True
)
