import os
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

# Define the folder containing the PDFs
folder_path = "data"

# Initialize the text splitter and embedding model
text_splitter = RecursiveCharacterTextSplitter(chunk_size=7500, chunk_overlap=100)
embedding_model = OllamaEmbeddings(model="nomic-embed-text", show_progress=True)

# Create a list to hold all document chunks
all_chunks = []

# Iterate over each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        # Load the PDF
        file_path = os.path.join(folder_path, filename)
        loader = UnstructuredPDFLoader(file_path=file_path)
        data = loader.load()

        # Split the document into chunks
        chunks = text_splitter.split_documents(data)
        
        # Add the chunks to the list
        all_chunks.extend(chunks)

# Add all chunks to the vector database
vector_db = Chroma.from_documents(
    documents=all_chunks, 
    embedding=embedding_model,
    collection_name="classes"
)
