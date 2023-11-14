from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import *


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'avatar', 'created_at', 'updated_at', 'nickname']
        extra_kwargs = {
            "created_at": {"ready_only": True},
            "updated_at": {"ready_only": True}
        }

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
        }


class SurvivorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survivor
        fields = [
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

class MonsterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monster
        fields = [
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
