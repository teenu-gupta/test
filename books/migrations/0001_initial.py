# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=400)),
                ('author', models.CharField(max_length=300)),
                ('inventory_count', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Book_Issue_Details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_of_issue', models.DateField(auto_now=True)),
                ('date_of_return', models.DateField()),
                ('book', models.ForeignKey(to='books.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('employee_name', models.CharField(max_length=400)),
                ('team', models.CharField(max_length=400)),
            ],
        ),
        migrations.AddField(
            model_name='book_issue_details',
            name='book_issued_to',
            field=models.ForeignKey(to='books.Employee'),
        ),
    ]
