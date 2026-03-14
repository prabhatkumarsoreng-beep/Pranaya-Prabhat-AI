import streamlit as st
import google.generativeai as genai

API_KEY = "AIzaSyDmuDEkXrSo_FsM1GTse1pslnYLmVh-rUM"

genai.configure(api_key=API_KEY)

st.set_page_config(page_title="Pranaya Prabhat AI", page_icon="👸")

st.title("👸 Pranaya Prabhat AI")
st.write("नमस्ते प्रभात सर जी! मैं आपकी सेवा में हाज़िर हूँ।")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("यहाँ लिखें...")

if prompt:

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.write(prompt)

    try:
        model = genai.GenerativeModel("models/gemini-1.5-flash")

        response = model.generate_content(prompt)

        answer = response.text

        with st.chat_message("assistant"):
            st.write(answer)

        st.session_state.messages.append({"role": "assistant", "content": answer})

    except Exception as e:
        st.error(f"Error आया है: {e}")
