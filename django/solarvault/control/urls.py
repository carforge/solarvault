from django.urls import path

from . import views

app_name = "control"
urlpatterns = [
    path("", views.psu_control, name ="index")
]