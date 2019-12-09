from django.urls import path
  
from . import views

urlpatterns = [
        path('', views.all_squirrels),
        path('add/', views.add_squirrel),
        path('stats/', views.stats),
        path('<str:unique_squirrel_id>/', views.update_squirrel),
]
