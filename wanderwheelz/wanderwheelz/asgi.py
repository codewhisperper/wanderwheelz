"""
ASGI config for wanderwheelz project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wanderwheelz.settings')

os.environ.setdefault('DB_NAME_DJANGO', 'ww-db')
os.environ.setdefault('DB_USER_DJANGO', 'root')
os.environ.setdefault('DB_PASSWORD_DJANGO', 'WanderWheelz@1234')
os.environ.setdefault('CLOUD_SQL_INSTANCE_IP', 'wander-wheelz:ww-db')
os.environ.setdefault('CLOUD_SQL_PORT', '3306')

application = get_asgi_application()
