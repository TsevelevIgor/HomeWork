from collections import Counter


def counted_category(transactions: list[dict]) -> dict:
    """Функция подсчитывает количество операций в категориях"""
    transactions_category = []
    category = dict(list)
    for transaction in transactions:
        category = transaction['description']
        transactions_category.append(category)
    counted = Counter(transactions_category)
    return counted
