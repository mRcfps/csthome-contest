from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Contestant
from .serializers import ContestantSerializer


class UserLoginView(APIView):
    """用户登录"""

    serializer_class = AuthTokenSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class ScoreBoardView(generics.ListAPIView):
    """获取所有选手的比分"""

    serializer_class = ContestantSerializer
    queryset = Contestant.objects.all()
