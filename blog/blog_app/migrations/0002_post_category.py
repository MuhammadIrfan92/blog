# Generated by Django 3.2.3 on 2021-06-03 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
