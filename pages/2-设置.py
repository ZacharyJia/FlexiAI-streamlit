import streamlit as st

st.title('设置')

api_base = st.text_input('api_base', value=st.session_state['api_base'], placeholder='https://xxx.com/v1')
if api_base:
    st.session_state['api_base'] = api_base

api_key = st.text_input('api_key', value=st.session_state['api_key'], placeholder='sk-xxx')
if api_key:
    st.session_state['api_key'] = api_key

models = [
    "gpt-3.5-turbo",
    "gpt-4",
    "claude-instant-v1",
    "claude-instant-v1-100k",
    "claude-2-100k",
]

model_index = 0
for i, m in enumerate(models):
    if m == st.session_state['model']:
        model_index = i
        break

model = st.selectbox('选择LLM模型', models, index=model_index)
if model:
    st.session_state['model'] = model
