# Generated by Django 2.2.12 on 2020-06-17 09:43

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=markdownx.models.MarkdownxField(verbose_name='Post Content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='read_time',
            field=models.IntegerField(blank=True, default=0, verbose_name='Read time'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True, verbose_name='Slug of post'),
        ),
    ]
