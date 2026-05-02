import os
import sys

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recipeglobe_project.settings")

# Setup Django fully before getting the app
import django
django.setup()

# Import and wrap the handler explicitly
from django.core.handlers.wsgi import WSGIHandler
app = WSGIHandler()