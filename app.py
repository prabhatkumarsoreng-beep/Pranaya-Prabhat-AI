import streamlit as st
import google.generativeai as genai

# आपकी API KEY
API_KEY = "AIzaSyDmuDEkXrSo_FsM1GTse1pslnYLmVh-rUM"

# Gemini चालू करना
genai.configure(api_key=API_KEY)

# Page setting
st.set_page_config(page_title="Pranaya AI", page_icon="👸")

# Title
st.title("👸 Pranaya Prabhat AI")
st.write("नमस्ते प्रभात सर जी! मैं आपकी सेवा में हाज़िर हूँ।")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if prompt := st.chat_input("यहाँ लिखें..."):
    
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.write(prompt)

    try:
        model = genai.GenerativeModel("gemini-1.5-flash-latest")

        response = model.generate_content(
            f"You are a helpful female assistant. Reply in friendly Hindi. User message: {prompt}"
        )

        answer = response.text

        with st.chat_message("assistant"):
            st.write(answer)

        st.session_state.messages.append({"role": "assistant", "content": answer})

    except Exception as e:
        st.error(f"Error आया है: {e}")
