import pytest
import requests

BASE_URL = "http://5.181.109.28:9090/api/v3"

@pytest.fixture(scope="function")
def create_pet():
    new_pet_data = {
        "id": 1,
        "name": "Buddy",
        "status": "available"
    }

    response = requests.post(url=f"{BASE_URL}/pet", json=new_pet_data)
    assert response.status_code == 200
    return response.json()