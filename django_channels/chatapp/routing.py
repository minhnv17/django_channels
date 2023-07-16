from django.urls import re_path
from . import consummers

websocket_urlpatterns = [
    re_path(r'ws/stream', consummers.ChatappConsummer.as_asgi())
]
