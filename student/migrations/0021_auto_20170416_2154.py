# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-16 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0020_auto_20170410_0847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashboard_activity_log',
            name='student',
        ),
        migrations.RenameField(
            model_name='student_activity_log_withscroll',
            old_name='scrollPoints1',
            new_name='scrollPoints',
        ),
        migrations.AddField(
            model_name='student_activity_log_withscroll',
            name='answerPostTimeStamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student_activity_log_withscroll',
            name='commentPostTimestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student_activity_log_withscroll',
            name='question',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student_activity_log_withscroll',
            name='scrollTimestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student_activity_log_withscroll',
            name='timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Dashboard_Activity_Log',
        ),
    ]
