from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

data = {
    "name": "Fazliddin Nabiyev",
    "due_date": "Today",
    "description": "string",
}


def test_create_todo():
    response = client.post("/todo/", json=data)
    assert response.status_code == 200
    assert response.json() == data


def test_get_all_todo():
    response = client.get("/todo/")
    assert response.status_code == 200
    assert data in response.json()


def test_get_todo():
    response = client.get("/todo/0")
    assert response.status_code == 200
    assert response.json() == data


def test_update_todo():
    response = client.put("/todo/0", json={
        "name": "Nabiyev Nabiyev",
        "due_date": "Today",
        "description": "Python",
    })
    assert response.status_code == 200
    assert response.json() == {
        "name": "Nabiyev Nabiyev",
        "due_date": "Today",
        "description": "Python",
    }


def test_delete_todo():
    response = client.delete("/todo/0")
    assert response.status_code == 200
    assert response.json() == {
        "name": "Nabiyev Nabiyev",
        "due_date": "Today",
        "description": "Python",
    }
