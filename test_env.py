from dotenv import load_dotenv
import os

load_dotenv()  # Automatically looks for a .env file in the current directory

api_key = os.getenv("OPENAI_API_KEY")  # ✅ No "./" — just the key name

if api_key:
    print("Loaded API Key:", api_key)
else:
    print("API Key not found. Make sure your .env file is in the correct directory and the key is properly set.")
