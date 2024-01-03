from django.urls import re_path
from .consumers import CheckInOutConsumer

websocket_urlpatterns = [
    re_path(r'ws/check_in_out/(?P<business_id>\d+)/$', CheckInOutConsumer.as_asgi()),
]