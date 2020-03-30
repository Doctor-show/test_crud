from data.views import *
from django.urls import path

urlpatterns = [
    path('data/create/', DataCreateView.as_view()),
    path('data/list/', DataListView.as_view()),
    path('data/check/<int:pk>/', DataDetailView.as_view()),
]

