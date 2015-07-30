from django.contrib import admin
from .models import Job, Talk, Publication, Education

admin.site.register(Job)
admin.site.register(Talk)
admin.site.register(Publication)
admin.site.register(Education)