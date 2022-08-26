from django.urls import re_path
from .views import EventListView

urlpatterns = [
    re_path('', EventListView.as_view(), name="EventListView"),
    # re_path('<int:name>', views.EventDetail.as_view()),
]