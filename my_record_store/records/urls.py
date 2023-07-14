from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('records/', views.records, name='records'),
    path('records/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),  
]
