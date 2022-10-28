from rest_framework import serializers
from ads.models import Ad, Category, Selection
from users.models import User


def check_is_false(value):
    if value is True:
        raise serializers.ValidationError(f'{value} should be False')


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdDetailSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Ad
        fields = '__all__'


class AdUpdateSerializer(serializers.ModelSerializer):
    # author = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    # category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())
    is_published = serializers.BooleanField(validators=[check_is_false])

    class Meta:
        model = Ad
        fields = '__all__'


##################################################

class SelectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ['name']


class SelectionDetailSerializer(serializers.ModelSerializer):
    items = AdSerializer(many=True)

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = '__all__'
