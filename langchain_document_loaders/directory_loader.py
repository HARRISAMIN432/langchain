from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

# Lazy load does not load all documents at once
# It loads only on demand
# Use it when dealing with large documents

for document in docs:
    print(document.metadata)