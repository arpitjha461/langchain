# ...existing code...
import os
from dotenv import load_dotenv
from langchain_openai import OpenAI

load_dotenv()
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY not set in environment")

llm = OpenAI(model="text-davinci-003", api_key=OPENAI_API_KEY)
print(llm("What is the national sport of India?"))

