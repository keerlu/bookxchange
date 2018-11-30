# Generated by Django 2.1.2 on 2018-11-29 23:16

import books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20181129_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[(books.models.LoanStatus('on loan'), 'on loan'), (books.models.LoanStatus('requested'), 'requested'), (books.models.LoanStatus('available'), 'available'), (books.models.LoanStatus('not available'), 'not available')], default=('AV', 'available'), max_length=100),
        ),
    ]
