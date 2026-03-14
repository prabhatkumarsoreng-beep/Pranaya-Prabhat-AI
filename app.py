import streamlit as st
import google.generativeai as genai

# आपकी फोटो 6825 वाली चाबी यहाँ डाल दी है
API_KEY = "AIzaSyDmuDEkXrSo_FsM1GTse1pslnYLmVh-rUM"

genai.configure(api_key=API_KEY)

st.set_page_config(page_title="Pranaya Prabhat AI", page_icon="👸")
st.title("👸 Pranaya Prabhat AI")
st.write("नमस्ते प्रभात सर जी! अब मैं पूरी तरह तैयार हूँ।")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("यहाँ लिखें प्रभात सर जी..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    try:
        # यहाँ हमने 'gemini-1.5-flash' का इस्तेमाल किया है
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(f"आप एक विनम्र महिला एआई सहायिका हैं। सरल हिंदी में जवाब दें: {prompt}")
        
        with st.chat_message("assistant"):
            st.write(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"ओह! अभी भी चाबी में कुछ दिक्कत है। एरर: {e}")
