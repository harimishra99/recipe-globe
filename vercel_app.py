import os
import sys

# Add the site-packages from uv's venv to the path
sys.path.insert(0, '/var/task/.vercel/python/.venv/lib/python3.12/site-packages')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recipeglobe_project.settings")

import django
django.setup()

from django.core.handlers.wsgi import WSGIHandler
app = WSGIHandler()