import os
import django
from django.core.wsgi import get_wsgi_application

os.environ["DJANGO_SETTINGS_MODULE"] = "recipeglobe_project.settings"
django.setup()

app = get_wsgi_application()