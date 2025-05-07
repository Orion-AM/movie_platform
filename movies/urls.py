from django.urls import path
from . import views

urlpatterns = [
    path('', views.public_list, name='public_list'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_movie, name='add_movie'),
    path('update/<int:pk>/', views.update_movie, name='update_movie'),
    path('delete/<int:pk>/', views.delete_movie, name='delete_movie'),
]
