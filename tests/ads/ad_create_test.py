import pytest


@pytest.mark.django_db
def test_create_ad(client, token, user):
    expected_response = {
        "id": 1,
        "name": "test_ad_name",
        "price": 100,
        "description": None,
        "is_published": False,
        "image": None,
        "author": user.pk,
        "category": None
    }

    data = {
        "name": "test_ad_name",
        "price": 100,
        "is_published": False,
        "author": user.pk
    }

    response = client.post(
        "/ad/create/",
        data=data,
        content_type="application/json",
        HTTP_AUTHORIZATION="Bearer " + token
    )

    assert response.status_code == 201
    assert response.data == expected_response
