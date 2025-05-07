def get_weather(city: str) -> str:
    data = {
        "Lagos": "30°C, sunny",
        "London": "15°C, cloudy",
        "New York": "22°C, rainy"
    }
    return data.get(city, "No weather data available for that city.")

# LangChain Tool wrapper
from langchain.agents import Tool

weather_tool = Tool(
    name="get_weather",
    func=get_weather,
    description="Use this tool to get the current weather in a given city."
)

