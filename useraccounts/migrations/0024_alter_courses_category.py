# Generated by Django 3.2.4 on 2021-07-06 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0023_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='category',
            field=models.CharField(choices=[('1', 'Đại Học - Cao Đẳng'), ('2', 'Bổ Trợ'), ('3', 'Luyện thi đại học'), ('4', 'Bồi dưỡng học sinh giỏi'), ('6', 'Từ lớp 6 đến lớp 9'), ('7', 'Luyện thi vào lớp 6'), ('8', 'Từ lớp 5 đến lớp 9'), ('9', 'Học nghe')], max_length=200, null=True),
        ),
    ]
