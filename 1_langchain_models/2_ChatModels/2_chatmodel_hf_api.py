from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("HUGGINGFACE_ACCESS_TOKEN"))

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_ACCESS_TOKEN")
)

model = ChatHuggingFace(llm=llm)

result = model.invoke([("human", "What is the capital of Pakistan?")])
print(result.content)