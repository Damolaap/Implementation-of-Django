# Generated by Django 4.1 on 2024-09-10 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUDAPP', '0008_alter_comment_comment_alter_comment_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_title',
            field=models.CharField(max_length=400),
        ),
    ]
