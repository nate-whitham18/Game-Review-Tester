import requests

BASE_URL = "http://localhost:3001"

def test_get_all_games():
    response = requests.get(f"{BASE_URL}/games")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "title" in data[0]

def test_post_new_review():
    new_review = {
        "gameId": 2,
        "rating": 4,
        "comment": "Pretty good!"
    }
    response = requests.post(f"{BASE_URL}/reviews", json=new_review)
    assert response.status_code == 201
    data = response.json()
    assert data["gameId"] == 2
    assert data["rating"] == 4
    assert data["comment"] == "Pretty good!"
    # Save ID for use in delete test
    global last_review_id
    last_review_id = data["id"]

def test_get_reviews():
    response = requests.get(f"{BASE_URL}/reviews")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert "rating" in data[0]

def test_delete_review():
    global last_review_id
    assert last_review_id is not None
    response = requests.delete(f"{BASE_URL}/reviews/{last_review_id}")
    assert response.status_code == 200


def test_post_review_missing_fields():
    # Missing rating
    bad_review = {
        "gameId": 1,
        "comment": "Missing rating field"
    }
    response = requests.post(f"{BASE_URL}/reviews", json=bad_review)
    assert response.status_code == 201  # json-server does not validate fields
    data = response.json()
    # Even though it returns 201, we can check that 'rating' is missing
    assert "rating" not in data or data["rating"] is None

def test_post_review_invalid_rating_type():
    bad_review = {
        "gameId": 1,
        "rating": "five stars",  # Invalid type
        "comment": "Rating is a string"
    }
    response = requests.post(f"{BASE_URL}/reviews", json=bad_review)
    assert response.status_code == 201
    # Again, json-server won't block it, so we manually validate
    assert isinstance(response.json()["rating"], str)

def test_delete_nonexistent_review():
    invalid_id = 99999
    response = requests.delete(f"{BASE_URL}/reviews/{invalid_id}")
    # json-server still returns 200, but we can check content
    assert response.status_code == 200
    assert response.text == '{}'

def test_get_invalid_endpoint():
    response = requests.get(f"{BASE_URL}/invalid-endpoint")
    assert response.status_code == 404