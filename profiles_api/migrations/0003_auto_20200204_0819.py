# Generated by Django 2.2 on 2020-02-04 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_auto_20200204_0816'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_active',
            new_name='is_activate',
        ),
    ]
