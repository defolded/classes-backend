from langchain.prompts import ChatPromptTemplate
from langchain_chroma import Chroma
from langchain_community.llms.ollama import Ollama
from .get_embedding_function import get_embedding_function

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

def query_llm(query_text: str, transcript_classes: list = None):
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    results = db.similarity_search_with_score(query_text, k=5)

    # Combine results with the student's classes if provided
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    
    if transcript_classes:
        # Extract text from Document objects
        student_classes_text = "\n".join([doc.get_content() for doc in transcript_classes])
        combined_context = f"{context_text}\n\nStudent's Completed Classes:\n\n{student_classes_text}"
    else:
        combined_context = context_text

    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=combined_context, question=query_text)

    model = Ollama(model="llama3.1")
    response_text = model.invoke(prompt)

    sources = [doc.metadata.get("id", None) for doc, _score in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    print(formatted_response)
    return response_text
