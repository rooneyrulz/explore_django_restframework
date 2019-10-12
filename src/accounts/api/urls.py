from django.urls import path, include
from knox import views as knox_views

from .views import RegisterAPI

app_name = 'accounts'
urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/register', RegisterAPI.as_view(), name='accounts-register')
]
