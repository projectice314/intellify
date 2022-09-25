from ctypes import Union
from typing import Type
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(quiz)



