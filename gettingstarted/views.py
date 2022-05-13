from django.shortcuts import render

# Create your views here.
from gettingstarted.serializers import *
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import viewsets
from .models import Verification


class GetStartedAPIView(viewsets.ModelViewSet):
    serializer_class = GetStartedSerializer
    queryset = Verification.objects.all()
    permission_classes = [AllowAny] #[IsAuthenticated]
    # serializer_class = GetStartedSerializer

    # def get_queryset(self):
    #     return self.request.user.verify.all()
    
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)
