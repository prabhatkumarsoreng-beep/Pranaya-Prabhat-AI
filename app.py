import streamlit as st
import google.generativeai as genai

# आपकी सही API KEY मैंने यहाँ डाल दी है
API_KEY = "AIzaSyAFgY5-MDv1BVlrPSSa9u8GyOier8V1Vzw"

genai.configure(api_key=API_KEY)

# पेज की सेटिंग
st.set_page_config(page_title="Pranaya Prabhat AI", page_icon="👸")

st.markdown("<h1 style='text-align: center;'>👸 Pranaya Prabhat AI</h1>", unsafe_allow_html=True)
st.write("नमस्ते प्रभात सर जी! मैं आपकी सहायिका हूँ।")

# चैट याद रखने के लिए
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# यूजर से इनपुट लेना
if prompt := st.chat_input("यहाँ लिखें प्रभात सर जी..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        # हिंदी में जवाब देने के लिए निर्देश
        full_prompt = f"आप एक विनम्र महिला एआई सहायिका हैं। प्रभात सर जी के सवालों का हमेशा सरल और बोलचाल वाली हिंदी में जवाब दें। सवाल: {prompt}"
        
        response = model.generate_content(full_prompt)
        
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error("माफ़ करना सर जी, कुछ तकनीकी दिक्कत आ गई है।")
