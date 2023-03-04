from django.urls import path, include
from usuario import views
urlpatterns = [
    path('listUser', views.ListUsers.as_view() )
]