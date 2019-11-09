import sys, os
#INTERP is present twice so that the new python interpreter
#knows the actual virtual environment path
INTERP = "/home/kane/.virtualenvs/caravanrouter/bin/python"

if sys.executable != INTERP:os.execl(INTERP, INTERP, *sys.argv)

cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd + '/caravanrouter')

sys.path.insert(0,cwd+'/home/kane/.virtualenvs/caravanrouter/bin')
sys.path.insert(0,cwd+'/home/kane/.virtualenvs/caravanrouter/lib/python2.7/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = "caravanrouter.settings"
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
