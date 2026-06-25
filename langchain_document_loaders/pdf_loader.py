from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

# It will return the same number of document objects as the number of pages in the PDF
# Each page will be a document object with its own page_content and metadata

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)