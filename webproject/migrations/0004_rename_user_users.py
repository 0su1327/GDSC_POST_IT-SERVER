# Generated by Django 4.1.7 on 2023-03-09 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webproject', '0003_alter_user_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Users',
        ),
    ]