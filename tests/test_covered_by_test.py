from fastapi.testclient import TestClient

from hello_poetry_and_nox.main import app

client = TestClient(app)


def test_read_covered_by_test():
    """Should return 200 and message."""
    response = client.get("/covered-by-test?covered=True")
    assert response.status_code == 200
    assert response.json() == {"message": "This path is covered by a test!"}


# def test_read_covered_by_test_with_no_query_param():
#     """Should return 200 and message."""
#     response = client.get("/covered-by-test")
#     assert response.status_code == 200
#     assert response.json() == {"message": "This path is not covered by a test!"}
