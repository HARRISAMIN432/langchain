# Import TextLoader to read text files and convert them into LangChain Documents
from langchain_community.document_loaders import TextLoader

# Import Gemini model wrapper for LangChain
from langchain_google_genai import ChatGoogleGenerativeAI

# Converts model output into a plain string
from langchain_core.output_parsers import StrOutputParser

# Used to create prompt templates with variables
from langchain_core.prompts import PromptTemplate

# Load environment variables from .env file
from dotenv import load_dotenv

# Used to access environment variables
import os


# Load variables from .env into the environment
load_dotenv()


# Create the Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("API_KEY"),  
    temperature=0.3                       
)


# Define a prompt template
# {poem} will be replaced with the contents of the text file
prompt = PromptTemplate(
    template="""
    Write a summary for the following poem:

    {poem}
    """,
    input_variables=["poem"]
)


# Convert model output into a normal Python string
parser = StrOutputParser()


# Create a loader for cricket.txt
loader = TextLoader(
    "./cricket.txt",
    encoding="utf-8"
)


# Load the file
# Returns a list of Document objects
docs = loader.load()


# Display information about the loaded documents
print("Type of docs:")
print(type(docs))

print("\nNumber of documents:")
print(len(docs))

print("\nDocument content:")
print(docs[0].page_content)

print("\nDocument metadata:")
print(docs[0].metadata)


# Create a LangChain pipeline:
# Prompt -> Gemini Model -> String Parser
chain = prompt | model | parser


# Run the chain
# docs[0].page_content contains the text from cricket.txt
result = chain.invoke({
    "poem": docs[0].page_content
})


# Print the generated summary
print("\nSummary:")
print(result)