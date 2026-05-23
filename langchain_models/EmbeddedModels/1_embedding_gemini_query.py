from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview",
    google_api_key=os.getenv("API_KEY"),
    dimensions=32
)

vector = embeddings.embed_query("What is AI?")
print(str(vector))

