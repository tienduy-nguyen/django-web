# Generated by Django 2.2.12 on 2020-06-17 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_userfollower'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='status',
            new_name='bio',
        ),
    ]
