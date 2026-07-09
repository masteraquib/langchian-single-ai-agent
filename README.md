# LangChain Single AI Agent

A simple Python project that demonstrates a conversational AI assistant built with Streamlit, LangChain, Groq, Tavily search, and WeatherStack.

## What this project does

This repository contains:

- A Streamlit-based chat interface in [app.py](app.py)
- A simple terminal/example script in [main.py](main.py)
- A notebook experiment in [notebook/single-ai-agent.ipynb](notebook/single-ai-agent.ipynb)

The assistant can:

- answer general questions
- search the web using Tavily
- fetch current weather information for a city using WeatherStack

## Project structure

- [app.py](app.py) — Streamlit web app for the AI assistant
- [main.py](main.py) — simple CLI/example version of the agent
- [requirements.txt](requirements.txt) — Python dependencies
- [notebook/single-ai-agent.ipynb](notebook/single-ai-agent.ipynb) — notebook version for experimentation

## Prerequisites

- Python 3.10 or newer
- A Groq API key
- A Tavily API key
- A WeatherStack API key

## Installation

1. Clone the repository

```bash
git clone <your-repo-url>
cd langchain-single-ai-agent
```

2. Create and activate a virtual environment

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

On macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

## Environment variables

Create a `.env` file in the project root with your API keys:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
WEATHERSTACK_API_KEY=your_weatherstack_api_key
```

> Make sure the `.env` file is not committed to Git.

## Run the Streamlit app

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

## Run the terminal example

```bash
python main.py
```

This runs a simple one-shot example using the same agent logic.

## Usage tips

- Ask the assistant general questions, such as:
  - "What is the capital of India?"
  - "What is the weather in London?"
  - "Find recent news about AI"
- The assistant will use the available tools when relevant.

## Troubleshooting

If the app does not start:

- verify your Python version
- confirm all dependencies were installed
- confirm your `.env` file contains valid API keys
- make sure your network connection allows API calls

## Notes

This project is intended for learning and experimentation with LangChain agents and tool calling in a small, practical example.
