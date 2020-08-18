# Generated by Django 2.2.12 on 2020-06-15 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFollower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followers', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='users.Profile')),
                ('following', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='users.Profile')),
            ],
        ),
    ]
