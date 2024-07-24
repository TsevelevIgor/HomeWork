import pytest


from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(lists_executed):
    assert filter_by_state(lists_executed) == [
        {'id': 111111111, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 999999999, 'state': 'EXECUTED', 'date': '2022-06-30T02:08:58.425572'}]


def test_sort_by_date(lists_date_down):
    assert sort_by_date(lists_date_down) == [
        {'id': 111111111, 'state': 'EXECUTED', 'date': '2022-07-03T18:35:29.512364'},
        {'id': 999999999, 'state': 'CANCELED', 'date': '2021-06-30T02:08:58.425572'},
        {'id': 123456789, 'state': 'EXECUTED', 'date': '2020-10-14T21:27:25.241689'},
        {'id': 324532455, 'state': 'CANCELED', 'date': '2019-10-14T08:21:33.419441'}]


def test_sort_same_date(lists_date):
    assert sort_by_date(lists_date) == [{'id': 111111111, 'state': 'EXECUTED', 'date': '2022-07-03T18:35:29.512364'},
                                        {'id': 999999999, 'state': 'CANCELED', 'date': '2022-07-03T18:35:29.512364'},
                                        {'id': 123456789, 'state': 'EXECUTED', 'date': '2020-10-14T21:27:25.241689'},
                                        {'id': 324532455, 'state': 'CANCELED', 'date': '2019-10-14T08:21:33.419441'}]
