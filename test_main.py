from fastapi.testclient import TestClient
from main import app  # Импортируй свое FastAPI приложение

client = TestClient(app)

def test_hashing_sha256_endpoint_positive_number():
    response = client.get("/hash/sha_256/123")
    assert response.status_code == 200
    assert response.json() == {
        "method": "sha_256",
        "number": 123,
        "hash": "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3"
    }

def test_hashing_sha256_endpoint_invalid_method():
    response = client.get("/hash/invalid_method/123")
    assert response.status_code == 400
    assert response.json() == {"detail": "The hashing method is specified incorrectly. Choose from 4 options: div, multi, universal, sha_256."}

def test_hashing_div_endpoint_invalid_number():
    response = client.get("/hash/div/Error")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["path", "number"],
                "msg": "Input should be a valid integer, unable to parse string as an integer",
                "type": "int_parsing",
                "input": "Error",
            }
        ]
    }

