# Generated by Django 3.2.4 on 2021-06-30 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0011_auto_20210626_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='benefit',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='courses',
            name='detail',
            field=models.TextField(default=''),
        ),
    ]
