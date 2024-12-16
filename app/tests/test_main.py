from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_test_run():
    response = client.post("/test_runs/", json={"test_suite_id": 1, "run_status": "in_progress"})
    assert response.status_code == 200
    assert response.json()["run_status"] == "in_progress"

def test_update_test_run():
    response = client.put("/test_runs/1", json={
        "result": "completed",
        "end_time": "2024-12-16T15:00:00",
        "test_results": [{"test_case_id": 1, "status": "pass"}]
    })
    assert response.status_code == 200
    assert response.json()["result"] == "completed"
