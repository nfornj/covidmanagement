import os
import time
os.environ.setdefault('DJANGO_SETTINGS_MODULE','covidcryindia.settings')
import django
django.setup()
from vaccination.tasks import delete_task, download_task,upload_task,remove_duplicated_records
delete_task.delay()

download_task.delay()
time.sleep(10)
upload_task.delay()

remove_duplicated_records.delay()
