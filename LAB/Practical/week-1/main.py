import os
from dotenv import load_dotenv
from google import genai

# Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

# Initialize Gemini client
client = genai.Client(api_key=api_key)

print("Connecting to Gemini...")

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
contents="Differentiate Artificial Intelligence, Machine Learning, and Deep Learning.")

    print("\n========== GEMINI RESPONSE ==========\n")
    print(response.text)

except Exception as e:
    print("\nGemini API request failed.")
    print("Error:", e)