"""
WSGI config for portal project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import dotenv
import tempfile
from django.core.wsgi import get_wsgi_application


dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bakerydemo.settings.dev")

_nativeEnvironment = os.environ.copy()


# make new tmp file securely so we can use it to communicate with the moralis
# backend using the fifo and not spinning up a new node every call....
#__tmpFile = tempfile.mkstemp()

# create the fifo

# Open the fifo for reading
#os.environ["SERVICE_TMPFILE"] = __tmpFile[1]

# Run the command to start the backend.
#cmd = "(cd /home/john/bakerydemo/moralis; node ./moralis-backend.js " +str(os.getpid()) + " " + __tmpFile[1] + " &)"
#print("Running: " + cmd)
#os.system(cmd)

# The website is inside here...
application = get_wsgi_application()
