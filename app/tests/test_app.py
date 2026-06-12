import pytest
import json
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, init_db

@pytest.fixture
def client():
    app.config["TESTING"] = True
    os.environ["DB_PATH"] = ":memory:"   # uses RAM — no file created
    with app.test_client() as client:
        with app.app_context():
            init_db()
        yield client

def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json["status"] == "healthy"

def test_create_task(client):
    r = client.post("/tasks",
        data=json.dumps({"title": "Buy groceries"}),
        content_type="application/json")
    assert r.status_code == 201

def test_get_tasks(client):
    client.post("/tasks",
        data=json.dumps({"title": "Test task"}),
        content_type="application/json")
    r = client.get("/tasks")
    assert r.status_code == 200
    assert len(r.json) >= 1

def test_create_task_no_title(client):
    r = client.post("/tasks",
        data=json.dumps({}),
        content_type="application/json")
    assert r.status_code == 400

def test_delete_task(client):
    client.post("/tasks",
        data=json.dumps({"title": "Delete me"}),
        content_type="application/json")
    r = client.delete("/tasks/1")
    assert r.status_code == 200