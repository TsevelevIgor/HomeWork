from collections import Counter


def counted_category(transactions: list[dict], caregory: list) -> dict:
    """Функция подсчитывает количество операций в категориях"""
    transactions_category = []
    for transaction in transactions:
        category = transaction['description']
        transactions_category.append(category)
    counted = Counter(transactions_category)
    return counted
