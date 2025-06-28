# products/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='product_home'),  # example route
]
