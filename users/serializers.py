from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Contestant


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password',)


class ContestantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contestant
        fields = ('user', 'name', 'score', 'logged')
