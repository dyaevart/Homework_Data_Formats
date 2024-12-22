import json
import xml.etree.ElementTree as ET
from pprint import pprint

def read_json(file_path, word_max_len=6, top_words_amt=10):
    """
    функция для чтения файла с новостями.
    """
    with open(file_path, encoding="utf-8") as f:
        json_data = json.load(f)
    news_list = [item["description"] for item in json_data["rss"]["channel"]["items"]]
    words_list = [new.split(" ") for new in news_list]
    all_words = [word for item in words_list for word in item]
    unique_words = set(all_words)

    popular = []
    for word in unique_words:
        if len(word) > 6:
            popular.append([word, all_words.count(word)])
    popular.sort(key=lambda x: x[1], reverse=True)

    return [item[0] for item in popular[:10]]

def read_xml(file_path, word_max_len=6, top_words_amt=10):
    """
    функция для чтения файла с новостями.
    """


if __name__ == '__main__':
    print(read_json('newsafr.json'))
    print(read_xml('newsafr.xml'))