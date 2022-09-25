from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from school.models import School, Classroom


# Create your models here.


class teacher_profile(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE, null=True, unique=True, related_name="teacherprofile")
    school = models.ForeignKey(School, null=True, on_delete=models.CASCADE, blank=True, unique=False, related_name="schoolprofile")
    img = models.ImageField(upload_to="teachers/", null=True, blank=True, default="t-avatar.jpg")
    full_name = models.CharField(max_length=50, null=True, default='')
    phone = models.CharField(max_length=50, blank=True, null=True, default='')
    gender = models.CharField(max_length=50, blank=True, null=True, default='')
    subject = models.CharField(max_length=100, blank=True, null=True, default='')
    address = models.TextField(blank=True, null=True, default='')
    zipcode = models.CharField(max_length=6, blank=True, null=True, default='')

    #updates
    classroom =  models.ManyToManyField(Classroom, null=True, blank=True, related_name="classroommodel")
    psw =  models.CharField(max_length=50, blank=True, null=True, default='')



    def __str__(self) :
        return self.full_name