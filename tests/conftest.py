import pytest


@pytest.fixture
def lists_executed():
    return [{'id': 111111111, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 999999999, 'state': 'EXECUTED', 'date': '2022-06-30T02:08:58.425572'},
            {'id': 123456789, 'state': 'CANCELED', 'date': '2021-10-14T21:27:25.241689'},
            {'id': 324532455, 'state': 'CANCELED', 'date': '2022-10-14T08:21:33.419441'}]


@pytest.fixture
def lists_date_down():
    return [{'id': 111111111, 'state': 'EXECUTED', 'date': '2022-07-03T18:35:29.512364'},
            {'id': 999999999, 'state': 'CANCELED', 'date': '2021-06-30T02:08:58.425572'},
            {'id': 123456789, 'state': 'EXECUTED', 'date': '2020-10-14T21:27:25.241689'},
            {'id': 324532455, 'state': 'CANCELED', 'date': '2019-10-14T08:21:33.419441'}]


@pytest.fixture
def lists_date():
    return [{'id': 111111111, 'state': 'EXECUTED', 'date': '2022-07-03T18:35:29.512364'},
            {'id': 999999999, 'state': 'CANCELED', 'date': '2022-07-03T18:35:29.512364'},
            {'id': 123456789, 'state': 'EXECUTED', 'date': '2020-10-14T21:27:25.241689'},
            {'id': 324532455, 'state': 'CANCELED', 'date': '2019-10-14T08:21:33.419441'}]
