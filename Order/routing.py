from django.urls import path
from .consumers import OrderConsumer

ws_patterns = [
    path('ws/orderstatus/<id>/', OrderConsumer.as_asgi())
]
