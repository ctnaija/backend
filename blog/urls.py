from django.urls import path, include
from .views import CompanyView, CompanyEdit

urlpatterns = [
    path('company/', CompanyView.as_view()),
    path('company/<int:id>', CompanyEdit.as_view()),
]
