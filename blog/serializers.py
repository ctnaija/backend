from rest_framework import serializers
from .models import Company, Post, Category, Comment


class CompanySerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Company
        fields = '__all__'
