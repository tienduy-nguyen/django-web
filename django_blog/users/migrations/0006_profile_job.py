# Generated by Django 2.2.12 on 2020-06-17 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200617_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='job',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
