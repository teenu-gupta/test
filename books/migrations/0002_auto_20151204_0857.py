# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_issue_details',
            name='status',
            field=models.CharField(default=True, max_length=200, choices=[(b'True', 'Issued'), (b'False', 'In Library')]),
        ),
        migrations.AlterField(
            model_name='book_issue_details',
            name='book_issued_to',
            field=models.ForeignKey(blank=True, to='books.Employee', null=True),
        ),
    ]
