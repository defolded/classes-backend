from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.1",
)

async def query_llm(messages):
    return await llm.ainvoke(messages)