from app.get_embedding_function import get_embedding_function
from langchain.prompts import ChatPromptTemplate
from langchain.vectorstores.chroma import Chroma
from langchain_community.llms.ollama import Ollama
from app.get_url_from_filename import get_url_from_filename
import os
from app.path import CHROMA_PATH


PROMPT_TEMPLATE = """
Отвечай на вопрос "{question}" на русском языке основываясь на следующем контексте:

{context}
"""


def query_rag(query_text: str):
    # Prepare the DB.
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_score(query_text, k=5)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    print("PROMPT:")
    print(prompt)

    model = Ollama(model="qwen2.5:3b", base_url="http://ollama:11434")
    response_text = model.invoke(prompt)

    sources = [doc.metadata.get("id", None) for doc, _score in results]
    processed_sources = []

    # Извлечение названий файлов и получение URL
    for path in sources:
        # Извлекаем имя файла (предполагаем, что оно всегда в начале строки до первого ':')
        filename = os.path.basename(path.split(":")[0])

        # Получаем URL по имени файла
        url = get_url_from_filename(filename)

        # Сохраняем результат в словаре
        processed_sources.append(url)

    result_sources_urls_string = "\n".join(processed_sources)

    formatted_response = (
        f"Ответ: {response_text}\n\nИсточники: {result_sources_urls_string}"
    )
    print(formatted_response)
    return formatted_response
