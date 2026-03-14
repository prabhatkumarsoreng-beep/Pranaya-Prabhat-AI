import streamlit as st
import google.generativeai as genai

# आपकी चाबी (API KEY)
API_KEY = "AIzaSyAFgY5-MDv1BVlrPSSa9u8GyOier8V1Vzw"

# एआई को चालू करना
genai.configure(api_key=API_KEY)

# ऐप की सजावट
st.set_page_config(page_title="Pranaya AI", page_icon="👸")
st.title("👸 Pranaya Prabhat AI")
st.write("नमस्ते प्रभात सर जी! मैं आपकी सेवा में हाज़िर हूँ।")

# मैसेज बॉक्स
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# सवाल पूछना
if prompt := st.chat_input("यहाँ लिखें..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        # सीधा और सरल जवाब
        response = model.generate_content(f"You are a helpful female assistant. Respond to '{prompt}' in friendly Hindi.")
        
        with st.chat_message("assistant"):
            st.write(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error("अभी भी कुछ गड़बड़ है। कृपया 'Manage app' में जाकर Logs देखें।")
