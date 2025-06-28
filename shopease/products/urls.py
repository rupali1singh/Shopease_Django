from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='product_home'),
    path('', views.product_list, name='product_list'),  # example route
]