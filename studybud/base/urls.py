from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('rooms/<str:pk>',views.room, name='room'),
    path('create-room/', views.createRoom, name="create-room"),
]
