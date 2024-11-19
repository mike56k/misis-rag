## RAG Сервис

Как запустить:

1. Скачать ollama https://ollama.com/
1. Скачать модели nomic-embed-text и mistral (через ollama pull)
1. Запустить модели ollama serve
1. Создать папку data в директории проекта
1. Добавить туда PDF файлы
1. Выполнить `python populate_database.py` для создания и наполнения векторной БД
1. Выполнить `python query_data.py "какой-нибудь вопрос"` для обращения к LLM с учетом данных из PDF
