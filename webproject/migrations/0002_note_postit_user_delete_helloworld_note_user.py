# Generated by Django 4.1.7 on 2023-03-09 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webproject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('note_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'note',
            },
        ),
        migrations.CreateModel(
            name='PostIt',
            fields=[
                ('postit_id', models.AutoField(primary_key=True, serialize=False)),
                ('writer', models.CharField(max_length=20)),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webproject.note')),
            ],
            options={
                'db_table': 'postit',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_email', models.CharField(max_length=30)),
                ('user_pw', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.DeleteModel(
            name='HelloWorld',
        ),
        migrations.AddField(
            model_name='note',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webproject.user'),
        ),
    ]
