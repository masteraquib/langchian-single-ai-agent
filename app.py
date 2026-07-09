import streamlit as st
import os
import requests
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from langchain.agents import create_agent
from langchain.tools import tool

# =========================
# Load Environment
# =========================

load_dotenv()

# =========================
# Page Config
# =========================

st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# =========================
# Header
# =========================

st.title("🤖 AI Assistant")
st.caption("Powered by Groq + LangChain + Tavily + WeatherStack")

# =========================
# Session State
# =========================

if "messages" not in st.session_state:
    st.session_state.messages = []

# =========================
# Sidebar
# =========================

with st.sidebar:

    st.title("⚙️ Settings")

    st.success("LLM : Groq")

    st.info("""
    Available Tools

    ✅ Web Search

    ✅ Weather

    """)

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# =========================
# LLM
# =========================

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.1-8b-instant",
    temperature=0,
    max_tokens=512,
)

# =========================
# Tavily
# =========================

search_tool = TavilySearch(
    max_results=2,
    topic="general",
    include_answer=True,
    include_raw_content=False,
)

# =========================
# Weather Tool
# =========================

WEATHERSTACK_API_KEY = os.getenv("WEATHERSTACK_API_KEY")


@tool
def get_weather_data(city: str) -> str:
    """
    Fetch current weather information.
    """

    url = (
        f"https://api.weatherstack.com/current"
        f"?access_key={WEATHERSTACK_API_KEY}"
        f"&query={city}"
    )

    response = requests.get(url)

    data = response.json()

    if "current" not in data:
        return "Unable to fetch weather."

    return f"""
City : {city}

Temperature : {data['current']['temperature']} °C

Weather : {data['current']['weather_descriptions'][0]}

Humidity : {data['current']['humidity']} %
"""


# =========================
# Agent
# =========================

agent = create_agent(
    model=llm,
    tools=[search_tool, get_weather_data],
    system_prompt="You are a helpful AI assistant."
)

# =========================
# Display Previous Messages
# =========================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# =========================
# Chat Input
# =========================

prompt = st.chat_input("Ask me anything...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("🤖 Thinking..."):

            response = agent.invoke(
                {
                    "messages": [
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                }
            )

            answer = response["messages"][-1].content

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )