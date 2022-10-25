import pytest


@pytest.mark.django_db
def test_create_selection(client, token):
    expected_response = {
        "id": 1,
        "name": "my_custom_selection",
        "author": 40,
        "items": [1, 5]
    }

    data = {
        "name": "my_custom_selection",
        "author": 40,
        "items": [1, 5]
    }

    response = client.post(
        "/selection/create/",
        data,
        content_type="application/json",
        HTTP_AUTHORIZATION="Bearer " + token
    )

    assert response.status_code == 201
    assert response.data == expected_response
