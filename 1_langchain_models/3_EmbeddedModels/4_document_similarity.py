from langchain_huggingface import HuggingFaceEmbeddings
import os
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = HuggingFaceEmbeddings(model='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "Virat Kohli is an Indian batsman known for chasing big targets with aggressive intent and maintaining high consistency across all formats of cricket.",
    "Babar Azam is a Pakistani top-order batsman recognized for his elegant cover drives, technical stability, and consistent run scoring in international matches.",
    "Steve Smith is an Australian Test specialist known for his unusual batting stance, extraordinary concentration, and dominance in red-ball cricket.",
    "Ben Stokes is an English all-rounder famous for delivering match-winning performances with both bat and ball, especially in high-pressure situations.",
    "Kane Williamson is a New Zealand captain admired for his calm temperament, classical batting technique, and ability to anchor innings for long durations."
]

doc_embeddings = embedding.embed_documents(documents)

query = input()

query_embed = embedding.embed_query(query)

scores = cosine_similarity([query_embed], doc_embeddings)[0] # Both should be in 2D form
index,score = sorted(list(enumerate(scores)), key=lambda x : x[1])[-1]

print(query)
print(documents[index])
print("Similarity Score: ", score)
