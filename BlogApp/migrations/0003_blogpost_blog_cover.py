# Generated by Django 4.1 on 2024-07-24 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0002_alter_blogpost_blog_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='blog_cover',
            field=models.ImageField(null=True, upload_to='blog_covers'),
        ),
    ]
