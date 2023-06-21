from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sign-up', views.registerPage, name="sign-up"),
    path('login', views.loginPage, name="login"),
    path('logout', views.logoutUser, name="logout")
]