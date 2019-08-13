# Generated by Django 2.2.3 on 2019-08-03 03:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190803_0307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 8, 3, 3, 41, 17, 795734, tzinfo=utc), verbose_name='post date'),
        ),
        migrations.AlterField(
            model_name='section',
            name='img',
            field=models.ImageField(default='images/post_default.jpg', upload_to='images/'),
        ),
    ]