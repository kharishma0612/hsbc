import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the Gemini API directly with the API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file.")

genai.configure(api_key=api_key)

# Create a GenerativeModel instance
model = genai.GenerativeModel('gemini-2.5-flash')

# Generate content
try:
    response = model.generate_content("Explain how AI works in a few words")
    print(response.text)
except Exception as e:
    print(f"An error occurred: {e}")
