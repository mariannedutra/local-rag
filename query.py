import argparse
from chromadb import HttpClient
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama

from embedding_function import get_embedding_function

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Primeiramente, analise esse contexto:
{context}

---------------

Agora, responda essa questão, se baseando no contexto fornecido anteriormente: 
{question}
"""


def main():
    # Create CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text
    query_rag(query_text)

def query_rag(query_text: str):
    # Prepare the DB.
    db = Chroma(persist_directory=CHROMA_PATH, collection_name='cleanedDocs',client=HttpClient(host='localhost', port=8000), embedding_function=get_embedding_function())

    # Search the DB.
    results = db.similarity_search_with_score(query_text, k=5)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    model = Ollama(model="llama3:8b-instruct-q8_0", base_url="http://localhost:11434")
    response_text = model.invoke(prompt)

    sources = [doc.metadata.get("id", None) for doc, _score in results]
    formatted_response = f"Resposta: {response_text}\nReferências: {sources}"
    print(formatted_response)
    return response_text


if __name__ == "__main__":
    main()