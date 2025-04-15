import pytest
from utils.hash_function import HashFunc

@pytest.fixture
def hash_func():
    return HashFunc()

def test_hash_with_sha_256_positive_number(hash_func):
    result = hash_func.hash_with_sha_256(123)
    assert result == "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3"

def test_hash_with_sha_256_negative_number(hash_func):
    result = hash_func.hash_with_sha_256(-456)
    assert result == "f536766480494f8b747c44f4ead0a341c48f53fca01e9073f65b219477652e82"

def test_hash_with_sha_256_zero(hash_func):
    result = hash_func.hash_with_sha_256(0)
    assert result == "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9"

def test_hash_with_div_zero(hash_func):
    result = hash_func.div_method(0)
    assert result == "0"

def test_hash_with_div_negative_number(hash_func):
    result = hash_func.div_method(-3)
    assert result == "16"

def test_hash_with_div_text(hash_func):
    result = hash_func.div_method(-3)
    assert result == "16"