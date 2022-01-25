"""
ASGI config for PushNotification project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from django.urls import path
from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from notification.consumers import TestConsumer
import notification.routing
import Order.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PushNotification.settings')

application = get_asgi_application()



application = ProtocolTypeRouter({
    # websocket urls will be handled by this websocket key
    'websocket': URLRouter(notification.routing.ws_patterns)
})

application = ProtocolTypeRouter({
    # websocket urls will be handled by this websocket key
    'websocket': AuthMiddlewareStack(URLRouter(
        Order.routing.ws_patterns
    ) )
})


