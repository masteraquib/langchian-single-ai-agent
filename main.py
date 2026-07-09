import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from langchain.agents import create_agent
from langchain.tools import tool
import requests

WEATHERSTACK_API_KEY =  os.getenv('WEATHERSTACK_API_KEY')

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.1-8b-instant",
    temperature=0,
    max_tokens=512,
)

search_tool = TavilySearch(
    max_results=2,
    topic="general",
    include_answer=True,
    include_raw_content=False,
)

@tool
def get_weather_data(city: str) -> str:
    """
    Fetch current weather information for a city.
    """

    url = (
        f"https://api.weatherstack.com/current?"
        f"access_key={WEATHERSTACK_API_KEY}&query={city}"
    )

    response = requests.get(url)

    data = response.json()

    if "current" not in data:
        return f"Could not fetch weather data for {city}"

    return (
        f"City: {city}\n"
        f"Temperature: {data['current']['temperature']}°C\n"
        f"Weather: {data['current']['weather_descriptions'][0]}\n"
        f"Humidity: {data['current']['humidity']}%"
    )

agent = create_agent(
    model=llm,
    tools=[search_tool, get_weather_data],
    system_prompt="You are a helpful AI assistant.",
)

response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Find the capital of India and then find its current weather"
            }
        ]
    }
)

print(response["messages"][-1].content)