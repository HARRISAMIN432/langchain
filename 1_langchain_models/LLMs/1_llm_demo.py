from dotenv import load_dotenv
load_dotenv()
import os
from langchain_google_genai import GoogleGenerativeAI

llm = GoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("API_KEY")
)

result = llm.invoke("What is the capital of Pakistan")
print(result)
