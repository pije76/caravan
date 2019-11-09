"""
WSGI config for caravanrouter project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os, sys

sys.path.append('/home/kane/public_html/caravanrouter')
sys.path.append('/home/kane/.virtualenvs/caravanrouter/lib/python2.7/site-packages')


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'caravanrouter.settings')

application = get_wsgi_application()
