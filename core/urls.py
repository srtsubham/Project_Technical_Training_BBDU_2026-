from django.urls import path

from .views import DV, LOV, LV, RV

urlpatterns = [
    path("", LV.as_view(), name="login"),
    path("logout/", LOV.as_view(), name="logout"),
    path("register/", RV.as_view(), name="register"),
    path("dashboard/", DV.as_view(), name="dashboard"),
]
