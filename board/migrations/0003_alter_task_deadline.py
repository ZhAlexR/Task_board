# Generated by Django 4.1.7 on 2023-04-16 21:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("board", "0002_alter_worker_position"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="deadline",
            field=models.DateTimeField(),
        ),
    ]
