from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework_mongoengine import serializers

from core.models.post import Post
from core.models.user import User


class UserSerializer(serializers.DocumentSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_active', 'is_staff')


class UserCreateSerializer(serializers.DocumentSerializer):
    password = CharField(required=True, write_only=True, validators=[validate_password])

    class Meta:
        model = User
        fields = '__all__'

    def validate_username(self, value):
        if User.objects.filter(username=value).first():
            raise ValidationError('Username already exists!')
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.password = make_password(password)
        user.save()
        return user


class PostSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class UserPostsSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title')
