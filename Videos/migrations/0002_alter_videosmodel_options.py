# Generated by Django 4.2.11 on 2024-05-26 08:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Videos", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="videosmodel",
            options={"verbose_name": "Video", "verbose_name_plural": "Videos"},
        ),
    ]