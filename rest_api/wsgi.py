"""
WSGI config for rest_api project.
WSGI（Web Server Gateway Interface）
Pythonにおいて、WebサーバとWebアプリケーションが通信するための、標準化されたインタフェース定義のこと

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from dj_static import Cling
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest_api.settings')

application = Cling(get_wsgi_application())
