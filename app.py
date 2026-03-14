import streamlit as st
import google.generativeai as genai

# आपकी चाबी यहाँ पहले से डाल दी है
API_KEY = "AIzaSyAFgY5-MDv1BVlrPSSa9u8GyOier8V1Vzw"

# एआई सेटअप
genai.configure(api_key=API_KEY)

# ऐप का नाम और सजावट
st.set_page_config(page_title="Pranaya Prabhat AI", page_icon="👸")
st.markdown("<h1 style='text-align: center;'>👸 Pranaya Prabhat AI</h1>", unsafe_allow_html=True)
st.write("नमस्ते प्रभात सर जी! मैं आपकी अपनी एआई सहायिका हूँ।")

# चैट की याददाश्त
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# प्रभात सर जी का सवाल
if prompt := st.chat_input("यहाँ लिखें प्रभात सर जी..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    try:
        # सबसे पक्का मॉडल इस्तेमाल कर रहे हैं
        model = genai.GenerativeModel('gemini-pro')
        
        # एआई को निर्देश कि वह आपसे हिंदी में बात करे
        full_instructions = f"प्रतिक्रिया दें: आप एक विनम्र महिला एआई सहायिका हैं। प्रभात सर जी के इस सवाल का सरल हिंदी में जवाब दें: {prompt}"
        
        response = model.generate_content(full_instructions)
        
        with st.chat_message("assistant"):
            st.write(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        
    except Exception as e:
        st.error(f"अभी भी तकनीकी दिक्कत है। एरर: {e}")
