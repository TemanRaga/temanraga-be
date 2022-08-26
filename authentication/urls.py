from django.urls import re_path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    re_path(r'^register/?$', RegisterView.as_view(), name='register'),
    re_path(r'^login/?$', LoginAPIView.as_view(), name='login'),
    re_path(r'^token/refresh/?$', TokenRefreshView.as_view(), name='token_refresh'),
]