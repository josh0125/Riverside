from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexPage, name='index'),
    path('plant_details', views.plantPage, name='plants'),
    path('category', views.categoryPage, name='categories'),
    path('about', views.aboutPage, name='about'),

    path('plant_details/<int:iID>', views.onePlantDisplayPage, name='plant'),
    path('category/<str:sName>', views.categoryDisplayPage, name='category'),
]