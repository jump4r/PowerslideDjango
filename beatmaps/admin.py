from django.contrib import admin

# Register your models here.
from .models import Submission, Beatmap

admin.site.register(Submission)
admin.site.register(Beatmap)
