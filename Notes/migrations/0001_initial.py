# Generated by Django 2.0.3 on 2018-03-11 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=120)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
