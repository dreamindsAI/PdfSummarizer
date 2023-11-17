from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import GooglePalmEmbeddings
from langchain.vectorstores import FAISS
from typing import List

def get_chunks(text: str) -> List[str]:
    """
    Split a given text into smaller chunks with specified overlap.

    Args:
        text (str): The input text to be split into chunks.

    Returns:
        List[str]: A list of text chunks.
    """
    # Create an instance of RecursiveCharacterTextSplitter with specified parameters
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )

    # Use the text splitter to split the input text into chunks
    chunks = text_splitter.split_text(text)

    return chunks

def get_vector_store(chunks: List[str]) -> FAISS:
    """
    Create and return a vector store using embeddings from GooglePalmEmbeddings.

    Args:
        chunks (List[str]): List of text chunks to create vectors from.

    Returns:
        FAISS: A vector store created from the text chunks using FAISS.
    """
    # Initialize GooglePalmEmbeddings
    embeddings = GooglePalmEmbeddings()

    # Create a vector store using FAISS from the given text chunks and embeddings
    vector_store = FAISS.from_texts(chunks, embeddings=embeddings)

    return vector_store