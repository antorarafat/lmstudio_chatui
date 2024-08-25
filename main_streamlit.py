import streamlit as st
import requests
import json

API_URL = "http://localhost:1234/v1/chat/completions"
MODEL = "lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf"

def get_bot_response(message, system_message, conversation_history):
    headers = {
        "Content-Type": "application/json"
    }
    
    messages = [
        {"role": "system", "content": system_message},
    ] + conversation_history + [
        {"role": "user", "content": message}
    ]
    
    data = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": -1,
        "stream": False
    }
    
    response = requests.post(API_URL, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code} - {response.text}"

st.set_page_config(page_title="LM Studio Chatbot", page_icon="🤖", layout="wide")

st.title("🤖 LM Studio Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "system_message" not in st.session_state:
    st.session_state.system_message = "You are a helpful assistant."

with st.sidebar:
    st.header("Settings")
    st.session_state.system_message = st.text_area("System Message", value=st.session_state.system_message, height=100)
    if st.button("Clear Conversation"):
        st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What's on your mind?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = get_bot_response(prompt, st.session_state.system_message, st.session_state.messages[:-1])
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})

st.markdown("---")
st.caption("Powered by LM Studio and Streamlit")