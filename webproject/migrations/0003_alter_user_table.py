# Generated by Django 4.1.7 on 2023-03-09 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webproject', '0002_note_postit_user_delete_helloworld_note_user'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
    ]
