import csv
import pandas as pd


def read_transactions_csv(file_name: str) -> list[dict]:
    """Считывает csv-файл и возвращает список словарей"""
    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        result = []
        for row in reader:
            result.append(row)
    return result


def read_transactions_excel(file_name: str) -> list[dict]:
    """Считывает excel-файл и возвращает список словарей"""
    reader = pd.read_excel(file_name)
    return reader
