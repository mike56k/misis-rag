# from langchain_community.embeddings.bedrock import BedrockEmbeddings
from langchain_community.embeddings.ollama import OllamaEmbeddings


def get_embedding_function():
    embeddings = OllamaEmbeddings(
        model="mxbai-embed-large", base_url="http://ollama:11434"
    )
    return embeddings
