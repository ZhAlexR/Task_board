# Generated by Django 4.1.7 on 2023-03-29 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("board", "0002_alter_position_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="worker",
            name="position",
            field=models.ForeignKey(
                default="Developer",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="workers",
                to="board.position",
            ),
        ),
    ]
