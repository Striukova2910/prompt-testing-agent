import streamlit as st
import choice2
import choice1


st.set_page_config(page_title="Prompt testing app", layout="centered")

page=st.sidebar.selectbox("Select page:",
                          ('Main','I want to test by myself','AI tests')
                          )

if page == 'Main':
    st.title("Main page")
    st.write("Welcome")
    st.markdown("""
    PromptLab is a tool for experimenting  
    with prompts in a flexible and interactive way.  

    You can:  
    • **Test directly:** Chat with the AI yourself to see how your prompt performs in real time.  
    • **Run AI-to-AI tests:** Select a test agent and let two AIs interact with each other, simulating user responses and revealing weaknesses or blind spots in your prompt.  

    This dual testing mode helps you refine your prompts faster, uncover edge cases, and improve reliability before deploying them in real scenarios.  

    Perfect for **prompt engineers**, **AI enthusiasts**, and **developers** who want to validate prompt quality with ease.
    """)

    st.image("PromptAgentStremlit/img/prompttest.jpg", caption="image prompt test", width=300)
elif page == 'I want to test by myself':
    st.title("I want to test by myself")
    choice1.by_myself()
elif page == 'AI tests':
    st.title("AI tests 💻")
    choice2.showWindow()

