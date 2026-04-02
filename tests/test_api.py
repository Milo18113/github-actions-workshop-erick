import pytest
from fastapi.testclient import TestClient
from app.endpoints import app
from app.endpoints import OperationRequest, OperationResponse

client = TestClient(app)

def test_sum_endpoint():
    response = client.post("/sum", json={"a": 2, "b": 3})
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 5

def test_resta_endpoint():
    response = client.post("/resta", json={"a": 10, "b": 4})
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 6

def test_multiplicacion_endpoint():
    response = client.post("/multiplicacion", json={"a": 4, "b": 5})
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 20