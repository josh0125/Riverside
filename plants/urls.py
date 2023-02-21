from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexPage, name='index'),
    path('plant_details', views.plantPage, name='plants'),
    path('category', views.categoryPage, name='categories'),
    path('about', views.aboutPage, name='about'),
    path('search', views.searchPage, name='search'),
    path('plant_details/search', views.searchPage, name='search'),
    path('category/search', views.searchPage, name='search'),

    path('plant_details/<int:iID>', views.onePlantDisplayPage, name='plant'),
    path('category/<str:sName>', views.categoryDisplayPage, name='category'),
]