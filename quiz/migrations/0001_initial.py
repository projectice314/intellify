# Generated by Django 4.0.3 on 2022-09-16 09:28

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacher', '0001_initial'),
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category_name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quistion_list', models.TextField(blank=True, null=True)),
                ('quiz_schedule', models.DateTimeField(default=datetime.datetime(2022, 9, 16, 14, 58, 22, 420622))),
                ('time_limit', models.IntegerField(blank=True, null=True)),
                ('no_of_questions', models.IntegerField(blank=True, null=True)),
                ('quiz_number', models.IntegerField(blank=True, null=True)),
                ('quiz_type', models.CharField(blank=True, max_length=50, null=True)),
                ('allowed_atempts', models.IntegerField(blank=True, default=1, null=True)),
                ('title', models.CharField(max_length=256)),
                ('student_list', models.TextField(blank=True, null=True)),
                ('classroom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.classroom')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.subjects')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher_profile')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question', models.CharField(max_length=500)),
                ('marks', models.IntegerField(default=1)),
                ('standard', models.CharField(blank=True, max_length=50, null=True)),
                ('chapter', models.CharField(blank=True, max_length=200, null=True)),
                ('topic', models.CharField(blank=True, max_length=200, null=True)),
                ('tags', models.CharField(blank=True, max_length=1000, null=True)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='level', to='quiz.category')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.subjects')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('answer', models.CharField(max_length=300)),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_answer', to='quiz.question')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]