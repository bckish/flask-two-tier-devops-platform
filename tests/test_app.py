from app import create_app


def test_local_database_round_trip(tmp_path):
    app = create_app({"TESTING": True, "DB_DRIVER": "sqlite", "SQLITE_PATH": str(tmp_path / "messages.db")})
    app.init_db()
    client = app.test_client()
    assert client.get("/health").json == {"status": "ok"}
    assert client.post("/submit", data={"new_message": "Hello local lab"}).json["message"] == "Hello local lab"
    assert b"Hello local lab" in client.get("/").data
    assert client.post("/submit", data={"new_message": "  "}).status_code == 400
