import os
import sys

# Adiciona o diretório raiz do projeto ao PATH do Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app


def test_health_check():
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Servidor no ar!"