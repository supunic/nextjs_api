"""
ASGI config for rest_api project.
ASGI（Asynchronous Server Gateway Interface）
WSGIの精神的な後継仕様であり、asyncioを介して非同期で動作するように設計されていて、またWebSocketなど複数のプロトコルをサポートしています。

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest_api.settings')

application = get_asgi_application()
