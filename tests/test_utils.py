from unittest.mock import patch, mock_open
from src.utils import get_transactions


@patch("builtins.open", new_callable=mock_open, read_data='{"transaction_id": 1}')
def test_get_transactions(file_path: str) -> None:
    transactions = get_transactions("test.json")
    assert transactions == {"transaction_id": 1}
