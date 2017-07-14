# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-14 13:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookIssueRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateField(auto_now=True)),
                ('due_date', models.DateField(null=True)),
                ('return_date', models.DateField(null=True)),
                ('fine_amount', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('isbn', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('copies_available', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('subscription_end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='bookissuerecord',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibraryManagement.Books'),
        ),
        migrations.AddField(
            model_name='bookissuerecord',
            name='borrower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibraryManagement.Borrower'),
        ),
        migrations.AddField(
            model_name='bookissuerecord',
            name='issuer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibraryManagement.Librarian'),
        ),
    ]
