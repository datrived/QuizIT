# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-01 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0015_auto_20170401_0852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_activity_log',
            name='question_list_time',
        ),
        migrations.RemoveField(
            model_name='student_activity_log',
            name='question_list_timestamp',
        ),
        migrations.AddField(
            model_name='dashboard_activity_log',
            name='activity_type',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dashboard_activity_log',
            name='question_list_time',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dashboard_activity_log',
            name='question_list_timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashboard_activity_log',
            name='dashboard_timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student_activity_log',
            name='retry_timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student_activity_log',
            name='review_timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student_activity_log',
            name='today_quiz_timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
