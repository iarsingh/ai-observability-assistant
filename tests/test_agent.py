from fastapi.testclient import TestClient
from obsassist.main import app

client = TestClient(app)


def test_runs_and_refuses_a_write():
    payload = client.post("/agent/run", json={"goal": 'why is latency high', **{'payload': {}}}).json()
    assert payload["refused"] is False
    assert payload["applied"] is False
    assert payload["board"] == "latency"
    refused = client.post("/agent/run", json={"goal": 'silence the alert'}).json()
    assert refused["refused"] is True
