from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #Login and logout
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #Dashboard
    path('', views.dashboard, name='dashboard'),
    #Change password
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]