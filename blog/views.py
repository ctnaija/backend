from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework import status
from rest_framework import generics, mixins
from rest_framework.response import Response
from .models import Company, Post, Category, Comment
from .serializers import CompanySerializer

class CompanyView(
    generics.GenericAPIView,
    mixins.ListModelMixin):

    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    def get(self, request):
        return self.list(request)


class CompanyEdit(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin):


    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    lookup_field = 'id'

    def get(self, request, id):
        return self.retrieve(request)

    def patch(self, request, id):
        return self.partial_update(request, id)

