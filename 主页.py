import streamlit as st

from plugins import weather, python_executor

st.title('Streamlit App')


if 'history' not in st.session_state:
    st.session_state['history'] = []

if 'api_base' not in st.session_state:
    st.session_state['api_base'] = ''


if 'api_key' not in st.session_state:
    st.session_state['api_key'] = ''

if 'model' not in st.session_state:
    st.session_state['model'] = 'gpt-4'

if 'selected_session' not in st.session_state:
    st.session_state['selected_session'] = 0

if 'sessions' not in st.session_state:
    st.session_state['sessions'] = []

if 'enabled_functions' not in st.session_state:
    st.session_state['enabled_functions'] = {
        'weather': {
            'name': 'weather',
            'callable': weather.call,
            'function_desc_for_model': weather.function_desc_for_model,
        },
        'python_executor': {
            'name': 'python_executor',
            'callable': python_executor.call,
            'function_desc_for_model': python_executor.function_desc_for_model,
        }
    }

st.write('当前已加载的函数：')
st.write(st.session_state['enabled_functions'])
