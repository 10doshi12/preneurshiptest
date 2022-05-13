from .serializers import *
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import viewsets
from .models import  school_student,college_student,configuration_manage,employed,configuration_manage


# Create your views here.
class school_view(viewsets.ModelViewSet,):
    queryset = school_student.objects.all()
    permission_classes = [AllowAny] #[IsAuthenticated]
    serializer_class = school_serializer
    # def get_queryset(self,owner1):
    #     return school_student.objects.filter(owner=owner1).all()

class college_view(viewsets.ModelViewSet):
    queryset = college_student.objects.all()
    permission_classes = [AllowAny] #[IsAuthenticated]
    serializer_class = college_serializer
    # def get_queryset(self):
    #     return college_student.objects.all()


class employed_view(viewsets.ModelViewSet):
    queryset = employed.objects.all()
    permission_classes = [AllowAny] #[IsAuthenticated]
    serializer_class = employed_serializer

class configuration_view(viewsets.ModelViewSet):
    queryset = configuration_manage.objects.all()
    permission_classes = [AllowAny] #[IsAuthenticated]
    serializer_class = configuration_serializer
