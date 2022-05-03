from django.urls import path

from user.views import RegistrationView
from user.views.obtain_auth_token import obtain_auth_token
from user.views.refresh_token_view import refresh_token_view
from user.views.logout_view import logout_view


urlpatterns = [
    #Авторизация / Регистрация
    path('registration/', RegistrationView.as_view()),
    path('login/', obtain_auth_token, name='api_login'),
    path('refresh/', refresh_token_view, name='api_refresh'),
    path('logout/', logout_view, name='api_logout'),
]
