from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# School Profile
# School Profile Model (Wasif)



class School(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name="schooluserprofile")
    name = models.CharField(max_length=100, null=True)
    hod_name = models.CharField(max_length=100, default="")
    students_no = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, null=True)
    date_created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.name)


class subjects(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    subject_id = models.CharField(max_length=10, null=True, blank=True)
    stream = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.name)

class Classroom(models.Model):
    standard = models.CharField(max_length=100, null=True, blank=True)
    classroom_id = models.CharField(max_length=10, null=True, blank=True)
    school_id = models.ForeignKey(School, null=True, on_delete=models.CASCADE, blank=True)
    section = models.CharField(max_length=100, null=True, blank=True)
    subject_list = models.ManyToManyField(subjects, null=True, blank=True, related_name="subjectmodel")

    def __str__(self):
        return str(self.standard) + str(self.section)



       
        