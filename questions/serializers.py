from rest_framework import serializers

from .models import Single, Multiple


class SingleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Single
        fields = ('id', 'question', 'answer')


class MultipleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Multiple
        fields = ('id', 'question', 'answer')
