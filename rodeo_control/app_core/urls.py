from django.urls import path
from app_core.views import general

app_name = 'app_core'
urlpatterns = [
    path('', general.index, name='index'),
    path('rodeo/<int:pk>/', general.rodeo, name='rodeo'),
    path('rodeo/<int:pk>/animales/', general.rodeo_animales, name='rodeo_animales'),
]