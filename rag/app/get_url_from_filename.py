import csv
from app.path import DATA_PATH
import os


def get_url_from_filename(filename):
    """Возвращает URL по имени файла из файла соотношений в формате CSV."""
    with open(
        os.path.join(DATA_PATH, "file_mapping.csv"), "r", encoding="utf-8"
    ) as mapping_file:
        csv_reader = csv.reader(mapping_file)
        next(csv_reader)  # Пропускаем заголовок
        for row in csv_reader:
            file_name, url = row
            if file_name == filename:
                return url
    return None
