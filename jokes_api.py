import json
import requests


def get_joke() -> str:
    """Получить анекдот с сайта rzhunemogu.ru.

    Возвращает:
        `str`: текст анекдота.
    """

    # Ссылка на API
    url = 'http://rzhunemogu.ru/RandJSON.aspx?CType=1'

    # Выполнение HTTP GET запроса к API
    response = requests.get(url)

    # Получение текста страницы
    text = response.text

    ########## ПЕРЕРАБОТКА ВОЗВРАТА API ##########
    # Убираем символ возврата каретки
    text = text.replace('\r', '')

    # Экранируем символ новой строки
    text = text.replace('\n', '\\n')

    # Временно заменяем все кавычки
    text = text.replace('"', '”')

    # Восстанавливаем структуру JSON, заменяя кавычки на двойные
    text = text.replace('”content”:”', '"content": "')
    text = text[::-1].replace('”', '"', 1)[::-1]

    # Сериализуем строку в словарь (str → dict)
    json_response = json.loads(text)

    # Возвращаем текст анекдота
    return json_response["content"]
