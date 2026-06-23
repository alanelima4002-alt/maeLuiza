from django.urls import path
from . import views

app_name = "maeLuiza"

urlpatterns = [
    path("", views.tela1, name="tela1"),
    path("tela2/", views.tela2, name="tela2"),
    path("tela3/", views.tela3, name="tela3"),
]