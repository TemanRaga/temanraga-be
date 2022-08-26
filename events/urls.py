from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', EventList.as_view()),
    path('<int:pk>/', EventDetail.as_view()),
]
