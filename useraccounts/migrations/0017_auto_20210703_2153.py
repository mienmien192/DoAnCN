# Generated by Django 3.2.4 on 2021-07-03 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0016_alter_comment_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='comment',
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useraccounts.student'),
        ),
    ]