from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview",
    google_api_key=os.getenv("API_KEY"),
    dimensions=32
)

documents = [
    "Islamabad is capital of Pakistan",
    "Shaheen Afridi is the ODI captain of Pakistan",
    "AI is speedily replacing software engineers",
    "We have to make posters for our EW Project"
]

vector = embeddings.embed_documents(documents)
print(str(vector))

