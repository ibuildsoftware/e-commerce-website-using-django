from django.urls import path
from core.views import index



app_name = "core" # name of application

urlpatterns = [
    path("", index) # homepage
]
