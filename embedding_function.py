import chromadb.utils.embedding_functions as embedding_functions

def get_embedding_function():

    embeddings= embedding_functions.OllamaEmbeddingFunction(
    url="http://localhost:11434/api/embeddings",
    model_name="nomic-embed-text",
    )
    
    return embeddings