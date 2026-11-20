
from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

print("Sending request to Gemini...")

response = client.models.generate_content(
    model=os.getenv("GEMINI_MODEL"),
    contents="Reply with exactly: Gemini is working!"
)

print("Gemini response:")
print(response.text)
