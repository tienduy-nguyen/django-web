# Generated by Django 2.2.12 on 2020-06-11 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200610_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
