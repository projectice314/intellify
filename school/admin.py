from django.contrib import admin
from .models import School, subjects, Classroom
# Register your models here.

admin.site.register(School)
admin.site.register(subjects)
admin.site.register(Classroom)