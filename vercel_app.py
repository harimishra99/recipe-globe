import os
import django
from django.core.handlers.wsgi import WSGIHandler

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recipeglobe_project.settings")
django.setup()

app = WSGIHandler()