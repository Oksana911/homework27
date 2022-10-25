import factory.django
from ads.models import Ad
from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    password = "12345"


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = "test_ad_name"
    price = 100
    is_published = False
    author = factory.SubFactory(UserFactory)

