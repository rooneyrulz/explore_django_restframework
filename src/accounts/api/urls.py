from django.urls import path, include
from knox import views as knox_views

from .views import RegisterAPI, LoginAPI, UserAPI

app_name = 'accounts'
urlpatterns = [
    path(
        'api/auth',
        include('knox.urls')
    ),
    path(
        'api/auth/register',
        RegisterAPI.as_view(),
        name='accounts-register'
    ),
    path(
        'api/auth/login',
        LoginAPI.as_view(),
        name='accounts-login'
    ),
    path(
        'api/auth/logout',
        knox_views.LogoutView.as_view(),
        name='accounts-logout'
    ),
    path(
        'api/auth/user',
        UserAPI.as_view(),
        name='accounts-user'
    )
]
