from app.path import DATA_PATH
import requests
from bs4 import BeautifulSoup
import os
import logging
import csv

# Настройка логирования
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Устанавливаем корневой URL и создаем множество для отслеживания посещенных страниц
root_url = "http://misis.ru"
visited = set()


def save_page(url):
    """Сохраняет HTML-код страницы в файл."""
    response = requests.get(url)
    if response.status_code == 200:
        # Создаем имя файла на основе URL
        filename = (
            url.replace("http://", "").replace("https://", "").replace("/", "_")
            + ".html"
        )
        filepath = os.path.join(DATA_PATH, filename)  # Путь к файлу в папке data
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(response.text)

        # Открываем файл для записи соотношения имени файла и URL в формате CSV
        mapping_file_path = os.path.join(DATA_PATH, "file_mapping.csv")

        # Проверяем, существует ли файл, чтобы не записывать заголовки повторно
        file_exists = os.path.isfile(mapping_file_path)

        with open(mapping_file_path, "a", newline="", encoding="utf-8") as mapping_file:
            csv_writer = csv.writer(mapping_file)
            # Записываем заголовки только если файл новый
            if not file_exists:
                csv_writer.writerow(["filename", "url"])
            csv_writer.writerow([filename, url])  # Записываем соотношение

        logging.info(f"Сохранена страница: {filepath}")
    else:
        logging.error(f"Ошибка при доступе к {url}: {response.status_code}")


def crawl(url, depth=0):
    """Рекурсивно обходит все ссылки на сайте с ограничением по глубине."""
    if depth > 1:  # Ограничение по глубине рекурсии
        logging.warning(f"Достигнута максимальная глубина рекурсии для {url}")
        return

    if url in visited or not url.startswith(root_url):
        return

    visited.add(url)  # Добавляем URL в посещенные
    save_page(url)  # Сохраняем страницу

    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            for link in soup.find_all("a", href=True):
                absolute_url = link["href"]
                # Приводим относительные ссылки к абсолютным
                if absolute_url.startswith("/"):
                    absolute_url = root_url + absolute_url
                crawl(
                    absolute_url, depth + 1
                )  # Рекурсивный вызов для каждой ссылки с увеличением глубины
    except Exception as e:
        logging.error(f"Ошибка при обработке {url}: {e}")
