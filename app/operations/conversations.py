from langchain.llm import GooglePalm
from langchain.memory import ConversationBufferMemory
from langchain.retrieval import ConversationalRetrievalChain
from langchain.vector_store import VectorStore

def get_conversational_chain(vector_store: VectorStore) -> ConversationalRetrievalChain:
    """
    Create and return a conversational chain for retrieval.

    Args:
        vector_store (VectorStore): The vector store used as a retriever.

    Returns:
        ConversationalRetrievalChain: A conversational chain for retrieval.
    """
    # Initialize GooglePalm language model
    llm = GooglePalm()

    # Initialize ConversationBufferMemory with memory_key and return_messages settings
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    # Create a conversational retrieval chain from LLM, vector_store retriever, and memory
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(),
        memory=memory
    )

    return conversation_chain
