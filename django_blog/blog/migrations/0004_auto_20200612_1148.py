# Generated by Django 2.2.12 on 2020-06-12 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200612_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='read_time',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
