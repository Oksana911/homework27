from rest_framework import serializers
from users.models import User, Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class UserListSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(required=False, read_only=True, many=True, slug_field='name')

    class Meta:
        model = User
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(required=False, many=True, read_only=True, slug_field='name')

    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(required=False,
                                            queryset=Location.objects.all(),
                                            many=True,
                                            slug_field="name")

    class Meta:
        model = User
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        self._location = self.initial_data.pop("location", []),
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        for loc in self._location:
            loc_obj, _ = Location.objects.get_or_create(name=loc)
            user.location.add(loc_obj)
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field="name"
    )

    class Meta:
        model = User
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        self._location = self.initial_data.pop("location", [])
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        user = super().save()

        for loc in self._location:
            loc_obj, _ = Location.objects.get_or_create(name=loc)
            user.location.add(loc_obj)
        user.save()
        return user


class UserDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']
