import streamlit as st
import google.generativeai as genai

# --- 1. API Key ---
API_KEY = "AIzaSyC_uSfW138HykGnXgr4nTnDFP JNPEIcqMk"
genai.configure(api_key=API_KEY)

# --- 2. Page Config ---
st.set_page_config(page_title="Pranaya Prabhat AI", page_icon="👸")

# --- 3. Style (Mobile Look) ---
st.markdown("""
<style>
.stApp { background-color: #fff0f5; }
.stChatMessage { border-radius: 15px; }
</style>
""", unsafe_allow_html=True)

# --- 4. Title ---
st.title("👸 Pranaya Prabhat AI")
st.write("नमस्ते प्रभात सर जी! मैं आपकी सहायिका हूँ।")

# --- 5. AI Settings ---
instruction = "आपका नाम 'Pranaya Prabhat AI' है। आप प्रभात सर जी की सहायिका हैं। हमेशा एक विनम्र महिला (Female) के लहजे में और सरल हिंदी में बात करें। प्रभात सर जी को हमेशा 'सर जी' कहकर बुलाएं।"

model = genai.GenerativeModel(model_name="gemini-1.5-flash", system_instruction=instruction)

# --- 6. Chat Logic ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("यहाँ लिखें प्रभात सर जी...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            reply = response.text
        except:
            reply = "माफ़ करना सर जी, कुछ तकनीकी दिक्कत आ गई है।"
        
        st.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})
        
    
