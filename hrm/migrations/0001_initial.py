# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-12 13:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AbsenceRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ins_date', models.DateTimeField(verbose_name='data di inserimento')),
                ('from_date', models.DateTimeField(verbose_name='data inizio')),
                ('to_date', models.DateTimeField(verbose_name='data fine')),
                ('total_days', models.IntegerField(default=0)),
                ('total_hours', models.IntegerField(default=0)),
                ('user_info', models.TextField()),
                ('status', models.CharField(choices=[('TO_APPROVE', 'Da approvare'), ('CANCELED_BY_USER', 'Cancellata dal richiedente'), ('NOT_APPROVED', 'Non approvata'), ('APPROVED', 'Approvata')], default='TO_APPROVE', max_length=25)),
                ('approver_info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AbsenceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.AddField(
            model_name='absencerequest',
            name='absence_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hrm.AbsenceType'),
        ),
        migrations.AddField(
            model_name='absencerequest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
