from django.shortcuts import render

# Create your views here.
from .serializers import *
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import viewsets
from .models import Portfolio

class GetStartedAPIView(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    permission_classes = [AllowAny] #[IsAuthenticated]
    serializer_class = PortfolioSerializer

    # def get_queryset(self):
    #     return self.request.user.verify.all()


