import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() #OpenAI API Key를 환경변수에서 가져오기

st.title("Chatbot with Streamlit")

# OpenAI API 객체 생성
client = OpenAI()

prompt = st.chat_input("입력해주세요.")
if prompt:
    messages = [
        {"role": "system", "content": "당신은 어시스턴트입니다"},
        {"role": "user", "content": prompt}
    ]

    # OpenAI API로 호출
    completion = client.chat.completions.create(
        model="gpt-4o-mini", #"gpt-4"
        messages=messages
    )
    
    # 대답 출력
    st.write(completion.choices[0].message.content)