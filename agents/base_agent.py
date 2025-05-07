import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("❌ OPENAI_API_KEY not found. Make sure it's in your .env file.")

# Updated import for LLM
from langchain_openai import OpenAI
from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType

# Import your custom tool
from tools.weather_tool import weather_tool

def run_agent(user_input: str) -> str:
    # Initialize the OpenAI LLM
    llm = OpenAI(
        temperature=0,
        openai_api_key=api_key
    )

    # Create an agent with the tool and model
    agent = initialize_agent(
        tools=[weather_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    # Let the agent handle the input
    return agent.run(user_input)

