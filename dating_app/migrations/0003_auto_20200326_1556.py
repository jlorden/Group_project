# Generated by Django 2.2 on 2020-03-26 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dating_app', '0002_auto_20200326_0230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile_page',
            old_name='like',
            new_name='likes',
        ),
    ]
