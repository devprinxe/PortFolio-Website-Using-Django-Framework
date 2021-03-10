"""
ASGI config for PortFolio project.
azie2-t=qvs+_+cbjp(7z0h5oiry%!9i$u93svm1@qnb!9ns7s
It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PortFolio.settings')

application = get_asgi_application()
