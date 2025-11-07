import streamlit as st
from llm import run_llm

st.set_page_config(page_title="Groq Chatbot", page_icon="🤖")

st.markdown("""
<style>
.chat-bubble-user {
    background-color: #DCF8C6;
    border-radius: 10px;
    padding: 8px 12px;
    margin: 6px 0px;
    width: fit-content;
    max-width: 75%;
}
.chat-bubble-ai {
    background-color: #F1F0F0;
    border-radius: 10px;
    padding: 8px 12px;
    margin: 6px 0px;
    width: fit-content;
    max-width: 75%;
}
</style>
""", unsafe_allow_html=True)


st.title("🤖 AI Chatbot (Groq+ LLaMA 3.1)")

#Initialize Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history= []


#User input
prompt= st.text_area("Your Prompt:", placeholder="Ask anything about AI research, trends, summaries...")


#Generate Response
if st.button("Send"):
    if prompt.strip():
        with st.spinner("Thinking....."):
            response= run_llm(prompt)

            #Save to Chat History
            st.session_state.chat_history.append(("You", prompt))
            st.session_state.chat_history.append(("AI", response))
    else:
        st.warning("Please type something first.")

#Display Chat History
st.write("---")
st.subheader("Chat History")

for role, message in st.session_state.chat_history:
    if role== "You":
        st.markdown(f"<div class= 'chat-bubble-user'><b>You:</b> {message}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class= 'chat-bubble-ai'><b>AI:</b> {message}</div>", unsafe_allow_html=True)