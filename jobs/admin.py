from django.contrib import admin
from .models import Job, Talk, Publication

admin.site.register(Job)
admin.site.register(Talk)
admin.site.register(Publication)