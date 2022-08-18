# Generated by Django 4.1 on 2022-08-18 02:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("snacks", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="snack",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
