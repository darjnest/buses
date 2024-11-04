from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("horarios/", views.lista_horarios, name="lista_horarios"),
    path("vender/<int:bus_id>/", views.vender_boleto, name="vender_boleto"),
    path("register/", views.register, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="ventas/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("mis_boletos/", views.mis_boletos, name="mis_boletos"),
    path("", views.home, name="home"),
    
]
