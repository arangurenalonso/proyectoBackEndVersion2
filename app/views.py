from django.shortcuts import render
from rest_framework import generics, views, permissions, viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework.parsers import MultiPartParser, FileUploadParser
from drf_yasg.openapi import Parameter, IN_QUERY, TYPE_STRING
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import status

from .serializers import CursorSerializer,WeekSerializer,CursoWeekSerializar, UnitSerializer
from .models import Curso, Week, Unit

#Amazon web service

#import boto3

# Create your views here.
class CursoViewSet(ListCreateAPIView):
    serializer_class = CursorSerializer
    queryset = Curso.objects.all()
    parser_classes = (MultiPartParser, FileUploadParser,)

    def post(self, request):
        return super(CursoViewSet,self).post(request)

class CursoRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CursorSerializer
    queryset = Unit.objects.all()
    parser_classes = (MultiPartParser, FileUploadParser,)
    lookup_field = "id"

class UnitViewSet(ListCreateAPIView):
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()
    parser_classes = (MultiPartParser, FileUploadParser,)

class UnitRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UnitSerializer
    queryset = Curso.objects.all()
    lookup_field = "id"

class WeekViewSet(ListCreateAPIView):
    serializer_class = WeekSerializer
    queryset = Week.objects.all()


class CursoWeekViewSet(RetrieveAPIView):
    serializer_class = CursoWeekSerializar
    queryset = Curso.objects.all()
    lookup_field = "id"