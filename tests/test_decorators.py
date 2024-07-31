import tempfile
from src.decorators import log


def test_log_good(capsys):
    @log()
    def func(x, y):
        return x + y
    result = func(1, 2)
    assert result == 3


def test_log_good_file_log(capsys):
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_file_path = tmp_file.name

    @log(filename=log_file_path)
    def func(x, y):
        return x + y
    func(1, 2)
    with open(log_file_path, 'r', encoding='utf-8') as file:
        logs = file.read()
    assert "my_function ok" in logs


def test_log_exception(capsys):
    @log()
    def func(x, y):
        return x + y
    func(1, "2")
    captured = capsys.readouterr()
    assert "my_function error" in captured.out


def test_log_exception_file_log(capsys):
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_file_path = tmp_file.name

    @log(filename=log_file_path)
    def func(x, y):
        return x + y
    func(1, "2")
    with open(log_file_path, 'r', encoding='utf-8') as file:
        logs = file.read()
    assert "my_function error" in logs
