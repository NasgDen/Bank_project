from unittest.mock import patch

from src.utils import read_json


@patch("json.load")
@patch("builtins.open")
def test_read_json(mock_open, mock_json):
    mock_json.return_value = {"key": "value"}
    assert read_json("test.json") == {"key": "value"}
    mock_open.assert_called_once_with("test.json", mode="r", encoding="utf-8")


@patch("json.load", side_effect=FileNotFoundError)
@patch("builtins.open")
def test_read_json_file_not_found(mock_open, mock_json):
    assert read_json("test.json") == []
    mock_open.assert_called_once_with("test.json", mode="r", encoding="utf-8")
