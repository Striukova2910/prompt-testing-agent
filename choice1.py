from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
import streamlit as st

def by_myself():
    st.title("User Testing")
    user_input = st.chat_input("Start the dialogue")

    def load_file_content(file):
        if not file:
            return ""
        try:
            file.seek(0)
            return file.read().decode('utf-8')
        except Exception as e:
            return f"⚠️ File reading error: {e}"

    with st.sidebar:
        st.header("🔧 Input data")

        def upload_and_edit(label, session_key, file_key=None, height=150):
            uploaded = st.file_uploader("f📂 {label}", type=["txt"], key=file_key)
            file_content = load_file_content(uploaded) if uploaded else ""
            if uploaded:
                st.code(file_content or "❌ The file is empty or unreadable.", language="text")
                if st.button(f"⬇️ Copy to {label}", key=session_key + "_copy"):
                    if file_content:
                        st.session_state[session_key] = file_content
                    else:
                        st.warning("⚠️ File doesn't have any content.")
            text_value = st.text_area(f"✏️ {label}", value=st.session_state.get(session_key, ""), height=height,
                                      key=session_key + "_text")
            st.session_state[session_key] = text_value

    with st.sidebar:
        seed_value = None
        SystemAI = st.radio("Select assistant mode:",
                                       ['gpt-4o', 'gpt-3.5-turbo'])

        seed_usage = st.radio("Choose if you need seed parameter. Seed parameter - a number that controls randomness in text generation.",
                     ['Yes', 'No'])
            #adding seed parameter
        if 'Yes' in seed_usage:
                seed_value = 100
        temperature_SystemAI = st.slider('Select temperature mode', min_value=0.0, max_value=2.0, step=0.1, key=1)
        upload_and_edit("System prompt", "System prompt", height=200)


    llm_parameters = {'model':SystemAI, 'temperature':temperature_SystemAI}
    if seed_value is not None:
        llm_parameters['seed'] = seed_value #'seed' - key, seed_value - meaning, llm_parameter[] - adding to dictionary


    llm = ChatOpenAI(**llm_parameters)
    # st.session_state - A dictionary in Streamlit that preserves data between page reloads.
    if "chat_memory" not in st.session_state:
        st.session_state.chat_memory = ConversationBufferMemory(return_messages=True)
    system_prompt = ChatPromptTemplate.from_messages([
        ("system", "you are math expert"),
        MessagesPlaceholder(variable_name="history"),
        ("user", "{input}")
    ])
    chain = LLMChain(llm=llm, prompt=system_prompt, memory=st.session_state.chat_memory)

    if user_input:
        response = chain.run(user_input)
        st.session_state.last_response = response
    if st.session_state.chat_memory.chat_memory.messages:
        for message in st.session_state.chat_memory.chat_memory.messages:
            if message.type == ("human"):
                st.chat_message("user").write(message.content) #human, assistant = emoji
            else:
                st.chat_message("assistant").write(message.content)

    """def load_file_content(file):
        if not file:
            return ""
        try:
            file.seek(0)
            return file.read().decode('utf-8')
        except Exception as e:
            return f"⚠️ Помилка читання файлу: {e}"
    with st.sidebar:
        st.header("🔧 Вхідні дані")
        def upload_and_edit(label,session_key, file_key=None,height=150):
            uploaded=st.file_uploader("f📂 {label}", type=["txt"], key=file_key)
            file_content = load_file_content(uploaded) if uploaded else ""
            if uploaded:
                st.code(file_content or "❌ Файл порожній або нечитабельний", language="text")
                if st.button(f"⬇️ Копіювати у {label}", key=session_key+"_copy"):
                    if file_content:
                        st.session_state[session_key] = file_content
                    else:
                        st.warning("⚠️ Файл не містить жодного тексту")
            text_value = st.text_area(f"✏️ {label}", value=st.session_state[session_key], height=height,
                                      key=session_key + "_text")
            st.session_state[session_key] = text_value

        upload_and_edit("Системний Промпт" , "system_prompt", file_key="file_system", height=200)
        SystemAI = st.radio("Обери режим бізнес агента:",
                                       ['gpt-4o', 'gpt-3.5-turbo'])
        temperature_SystemAI = st.slider('Select temperature mode', min_value=0.0, max_value=2.0, step=0.1, key=1)
        st.sidebar.markdown("---")"""