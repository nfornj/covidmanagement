import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','covidcryindia.settings')
import django
import django.setup()

import random
from covidfeed.models import Plasma,PlasmaTopic
from faker import Faker

fakegen = Faker()

PlasmaTopic = []


