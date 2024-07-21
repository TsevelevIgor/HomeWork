from typing import Any


list_of_dicts = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                 {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                 {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def filter_by_state(list_of_dicts: list[dict[str, Any]], state_by_key: str = 'EXECUTED') -> list[dict[str, Any]]:
    """Функция сортирует список по ключу state"""
    new_list = []
    for item in list_of_dicts:
        if item.get('state') == state_by_key:
            new_list.append(item)
    return new_list


def sort_by_date(list_of_dicts: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Функция сортирует список по дате"""
    sorted_by_date = sorted(list_of_dicts, key=lambda list_of_dicts: list_of_dicts['date'], reverse=reverse)
    return sorted_by_date
