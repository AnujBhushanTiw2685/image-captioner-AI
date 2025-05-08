import streamlit as st
from captioner import generate_caption

st.title("🖼️ AI Image Caption Generator")
st.write("Upload an image and get an AI‑generated description!")

# 1. File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])

if uploaded_file is not None:
    # 2. Display image
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    # 3. Generate and show caption
    with st.spinner("Generating caption..."):
        caption = generate_caption(uploaded_file)
    st.success("Caption:")
    st.write(f"**{caption}**")
