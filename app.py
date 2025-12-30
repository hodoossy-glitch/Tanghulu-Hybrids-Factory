import streamlit as st

st.set_page_config(
    page_title="Hybrid Creature Prompt Generator",
    page_icon="🧊🐾",
    layout="centered"
)

st.title("🧬 Hybrid Creature Image Prompt Generator")
st.write(
    "오브젝트 + 동물 하이브리드 설명을 입력하면\n"
    "Tanghulu 글레이즈가 적용된 **이미지 생성 프롬프트**를 자동으로 만들어줍니다."
)

# User input
hybrid_description = st.text_input(
    "Hybrid Creature Description",
    placeholder="예: Fridge Hippo, Toaster Crocodile, Washing Machine Cat"
)

# Generate prompt
if hybrid_description:
    image_generation_prompt = f"""
You are an expert image generation prompt engineer, specializing in hyper-detailed, photorealistic visual descriptions.

Create a single, comprehensive image generation prompt based on the following hybrid creature description.

Hybrid Creature Description:
{hybrid_description}

The image should depict a unique hybrid creature where the animal’s anatomical features are replaced or merged with components of the specified object.
Describe in detail how the object’s materials replace the animal’s body parts.

All surfaces of the creature must be coated in a thick, ultra-glossy, squishy Tanghulu-like glaze.
The glaze should look translucent, candy-coated, reflective, slightly bulging, and sticky, as if dipped in hardened sugar syrup.

Use realistic lighting, cinematic shadows, reflections, shallow depth of field, and photorealistic textures.
The creature should feel physically real despite its surreal form.
The background should be clean or cinematic and not distracting.

Generate a single, high-quality, photorealistic image.

IMPORTANT: Generate exactly one image
""".strip()

    st.subheader("📸 Image Generation Prompt")
    st.text_area(
        label="Copy & paste this into your image model",
        value=image_generation_prompt,
        height=420
    )

    st.success("프롬프트 생성 완료! 복사해서 바로 사용하세요 🚀")

else:
    st.info("하이브리드 설명을 입력하면 프롬프트가 생성됩니다.")
