# Generated by Django 3.2.3 on 2021-05-19 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('created_time', models.TimeField(auto_now_add=True)),
                ('last_update_time', models.TimeField(auto_now=True)),
            ],
        ),
    ]
