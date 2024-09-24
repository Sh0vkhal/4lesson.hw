from django.contrib import admin
from django.urls import path

from .views import ListAPIMoview, ListAPIComment

urlpatterns = [
    path('moview/',ListAPIMoview.as_view()),
    path('moview/<int:pk>/', ListAPIMoview.as_view()),
    path('comment/', ListAPIComment.as_view()),
    path('comment/<int:pk>/', ListAPIComment.as_view()),
]
