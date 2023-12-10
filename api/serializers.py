from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from core.models import *


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "date_joined",
            "is_active",
            "is_staff",
            "password",
        ]
        extra_kwargs = {
            "email": {"required": True},
            "password": {"write_only": True},
            "is_staff": {"read_only": True},
        }
        

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ['id', 'user', 'avatar', 'created_at', 'updated_at', 'nickname']
        extra_kwargs = {
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
            "user": {"read_only": True}
        }


class SurvivorSerializer(serializers.ModelSerializer):
    author = ProfileSerializer()
    class Meta:
        model = Survivor
        fields = [
            'id',
            'author',
            'author_comment',
            'cover',
            'created_at',
            'updated_at',
            'name',
            'codename',
            'characteristics',
            'torments',
            'conviction',
            'conditions',
        ]
        extra_kwargs = {
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
            "author": {"required": False},
            "cover": {"required": False},
            "codename": {"required": False},
        }

class MonsterSerializer(serializers.ModelSerializer):
    author = ProfileSerializer()
    class Meta:
        model = Monster
        fields = [
            'id',
            'author',
            'author_comment',
            'cover',
            'created_at',
            'updated_at',
            'name',
            'characteristics',
            'remaining_torments',
            'conditions',
        ]
        extra_kwargs = {
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
            "author": {"required": False},
            "cover": {"required": False},
            "remaining_torments": {"required": False},
        }


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user
    
    
# class SearchResultsSerializer(serializers.Serializer):
#     monsters = serializers.ListField(child=MonsterSerializer(), default=[])
#     survivors = serializers.ListField(child=SurvivorSerializer(), default=[])