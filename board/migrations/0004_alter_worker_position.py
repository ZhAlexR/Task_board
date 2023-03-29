# Generated by Django 4.1.7 on 2023-03-29 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("board", "0003_alter_worker_position"),
    ]

    operations = [
        migrations.AlterField(
            model_name="worker",
            name="position",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="workers",
                to="board.position",
            ),
        ),
    ]
