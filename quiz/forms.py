from django.forms import ModelForm
from .models import *

class QuestionsForm(ModelForm):
    class Meta:
        model = Question 
        fields = "__all__"
        exclude = ['uid']

class AnswerForm(ModelForm):
    class Meta:
        model = Answer 
        fields = "__all__"