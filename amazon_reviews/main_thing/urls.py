from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path("url_check", views.url_check, name="url_check")
    ]