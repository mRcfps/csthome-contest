from rest_framework import generics

from . import models, serializers


class SingleQuestionView(generics.RetrieveAPIView):

    queryset = models.Single.objects.all()
    serializer_class = serializers.SingleSerializer


class MutipleQuestionView(generics.RetrieveAPIView):

    queryset = models.Multiple.objects.all()
    serializer_class = serializers.MultipleSerializer
