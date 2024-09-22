import re


def filtered_operations(list_of_dict: list[dict], status: str) -> list[dict]:
    """Функция принимает список словарей с данными о банковских операциях и строку
    поиска и возвращает список словарей в которых есть эта строка."""
    result = []
    for operation in list_of_dict:
        if re.search(status, operation['description'], flags=re.IGNORECASE):
            result.append(operation)
    return result
