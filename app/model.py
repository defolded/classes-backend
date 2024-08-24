from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOllama
from langchain.retrievers.multi_query import MultiQueryRetriever
from .loader import vector_db

# Initialize LLM
llm = ChatOllama(model="llama3.1")

# Define the query prompt template
QUERY_PROMPT = PromptTemplate(
    input_variables=["question"],
    template="""You are an AI language model assistant. Your task is to generate five
    different versions of the given user question to retrieve relevant documents from
    a vector database. By generating multiple perspectives on the user question, your
    goal is to help the user overcome some of the limitations of the distance-based
    similarity search. Provide these alternative questions separated by newlines.
    Original question: {question}""",
)

retriever = MultiQueryRetriever.from_llm(
    vector_db.as_retriever(), 
    llm,
    prompt=QUERY_PROMPT
)

# RAG prompt template
RAG_PROMPT_TEMPLATE = """Answer the question based ONLY on the following context:
{context}
Question: {question}
"""

prompt = ChatPromptTemplate.from_template(RAG_PROMPT_TEMPLATE)

async def query_llm(prompt: str):
    # Retrieve relevant documents based on the prompt
    context_documents = retriever.get_relevant_documents(prompt)
    
    # Combine the context documents into a single string
    context_str = "\n".join([doc.page_content for doc in context_documents])
    
    # Prepare the input string for the LLM
    input_str = f"Context: {context_str}\nQuestion: {prompt}"
    
    # Invoke the model with the input string
    response = await llm.ainvoke(input_str)
    
    # Parse the model's response and return it
    parsed_response = StrOutputParser().parse(response)
    
    return parsed_response  # Return the parsed response, assumed to be a string
