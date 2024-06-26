## Conversational Q&A Chatbot

import streamlit as st 
from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain.chat_models import ChatOpenAI

## streamlit UI

st.set_page_config(page_title="ChatBot")
st.header("Hey, Lets Chat")

from dotenv import load_dotenv
load_dotenv()

import os

chat=ChatOpenAI(temperature=0.5)


if "flowmessages" not in st.session_state:
    st.session_state["flowmessages"]=[
        SystemMessage(content="You are a comedian AI assistant")
    ]


def get_chatmodel_response(question):
    
    st.session_state["flowmessages"].append(HumanMessage(content=question))
    answer=chat(st.session_state["flowmessages"])
    st.session_state["flowmessages"].append(AIMessage(content=answer.content))
    return answer.content


input=st.text_input("Input: ",key="input")
response = get_chatmodel_response(input)

submit=st.button("Ask the question")


## if ask button is clicked

if submit:
    st.subheader("The response is")
    st.write(response)