from fastapi.testclient import TestClient
from app import app

def test_generate_api(tmp_path, monkeypatch):
    monkeypatch.setattr("src.config.settings.output_dir", str(tmp_path), raising=False)
    c=TestClient(app); r=c.post("/generate",json={"concept":"box breathing with four steps","seed":7})
    assert r.status_code==200; body=r.json(); assert body["backend"]=="mock-pillow"; assert body["image_path"].endswith(".png")
