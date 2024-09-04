from unittest.mock import patch
from src.readers import read_transactions_csv, read_transactions_excel


@patch('csv.reader')
def test_read_transactions_csv(mock_reader):
    mock_reader.return_value = ['4699552', 'EXECUTED', '2022-03-23T08:29:37Z', '23423', 'Peso', 'PHP',
                                'Discover 7269000803370165', 'American Express 1963030970727681',
                                'Перевод с карты на карту']
    result = read_transactions_csv('../transactions.csv')
    expected_result = ['4699552', 'EXECUTED', '2022-03-23T08:29:37Z', '23423', 'Peso', 'PHP',
                       'Discover 7269000803370165', 'American Express 1963030970727681', 'Перевод с карты на карту']
    assert result == expected_result


@patch('pandas.read_excel')
def test_read_transactions_excel(mock_reader):
    mock_reader.return_value = {'id': 4699552.0, 'state': 'EXECUTED', 'date': '2022-03-23T08:29:37Z',
                                'amount': 23423.0,
                                'currency_name': 'Peso', 'currency_code': 'PHP', 'from': 'Discover 7269000803370165',
                                'to': 'American Express 1963030970727681', 'description': 'Перевод с карты на карту'}
    result = read_transactions_excel('../transactions_excel.xlsx')
    expected_result = {'id': 4699552.0, 'state': 'EXECUTED', 'date': '2022-03-23T08:29:37Z', 'amount': 23423.0,
                       'currency_name': 'Peso', 'currency_code': 'PHP', 'from': 'Discover 7269000803370165',
                       'to': 'American Express 1963030970727681', 'description': 'Перевод с карты на карту'}
    assert result == expected_result
