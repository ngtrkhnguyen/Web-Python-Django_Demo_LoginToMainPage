from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("mainpage/", views.mainpage_view, name="mainpage"),
    path("logout/", views.logout_view, name="logout"),
]