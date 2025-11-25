from django.urls import path
from .views import htmx_feed, htmx_like

urlpatterns = [
    path('', htmx_feed, name='htmx-feed'),
    path('like/', htmx_like, name='htmx-like'),
]

