# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20151204_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_issue_details',
            name='date_of_return',
            field=models.DateField(null=True),
        ),
    ]
