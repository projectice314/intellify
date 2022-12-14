# Generated by Django 4.0.3 on 2022-09-16 10:55

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='id',
        ),
        migrations.AddField(
            model_name='quiz',
            name='quiz_id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='quistion_list',
        ),
        migrations.AddField(
            model_name='quiz',
            name='quistion_list',
            field=models.ManyToManyField(blank=True, null=True, to='quiz.question'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='quiz_schedule',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 16, 16, 25, 6, 158344)),
        ),
    ]
