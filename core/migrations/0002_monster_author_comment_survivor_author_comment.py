# Generated by Django 4.1.5 on 2023-11-14 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='monster',
            name='author_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='survivor',
            name='author_comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
