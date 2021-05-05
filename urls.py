from django.urls import path
from ownerapp import views

urlpatterns = [
    path("oregister/", views.oregister , name = "ologin"),
]