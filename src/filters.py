import json
import re


def filtere_operations(list_of_dict: str, status: str) -> list[dict]:
    """Функция принимает список словарей с данными о банковских операциях и строку
    поиска и возвращает список словарей в которых есть эта строка."""
    with open(list_of_dict, encoding='utf-8') as s:
        data = json.load(s)
        operations = []
        for i in data:
            if i.get('state'):
                operations.append(i)
        return [trans for trans in operations if re.search(status, trans['state'])]
