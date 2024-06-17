from django.urls import path

from . import views

app_name = "read_state"
urlpatterns = [
    path("", views.read_data, name ="read_data")
]