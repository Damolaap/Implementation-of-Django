# Generated by Django 4.1 on 2024-07-04 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='blog_date',
            field=models.DateField(),
        ),
    ]
