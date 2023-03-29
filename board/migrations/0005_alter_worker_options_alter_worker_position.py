# Generated by Django 4.1.7 on 2023-03-29 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("board", "0004_alter_worker_position"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="worker",
            options={"verbose_name": "worker", "verbose_name_plural": "workers"},
        ),
        migrations.AlterField(
            model_name="worker",
            name="position",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="workers",
                to="board.position",
            ),
        ),
    ]