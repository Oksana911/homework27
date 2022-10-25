import pytest


@pytest.mark.django_db
def test_retrieve_ad(client, ad, token):
    expected_response = {
        "id": ad.pk,
        "name": "test_ad_name",
        "price": 100,
        "description": None,
        "is_published": False,
        "image": None,
        "author": ad.author.username,
        "category": ad.category_id
    }

    response = client.get(
        f"/ad/{ad.pk}/",
        HTTP_AUTHORIZATION="Bearer " + token
    )

    assert response.status_code == 200
    assert response.data == expected_response
