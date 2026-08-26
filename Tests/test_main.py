import sys
import os

# Permite importar main.py desde la carpeta App/
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'App'))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensaje": "API funcionando correctamente"}
    #   assert response.json() == {"mensaje": "Este texto está mal a propósito"}

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_usuarios():
    response = client.get("/usuarios")
    assert response.status_code == 200
    data = response.json()
    assert "usuarios" in data
    assert len(data["usuarios"]) == 2   

# def test_get_usuario_existente():
#     response = client.get("/usuarios/1")
#     assert response.status_code == 200
#     assert response.json() == {"id": 1, "nombre": "Ana"}

# def test_get_usuario_no_existente():
#     response = client.get("/usuarios/99")
#     assert response.status_code == 200
#     assert response.json() == {"error": "Usuario no encontrado"}