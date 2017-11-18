from rest_framework import generics

from . import models, serializers


class SingleQuestionView(generics.RetrieveAPIView):
    """根据序号获取单选题（1~90）"""

    queryset = models.Single.objects.all()
    serializer_class = serializers.SingleSerializer


class MutipleQuestionView(generics.RetrieveAPIView):
    """根据序号获取多选题（1~47）"""

    queryset = models.Multiple.objects.all()
    serializer_class = serializers.MultipleSerializer
