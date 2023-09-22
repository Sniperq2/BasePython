# Generated by Django 4.2.5 on 2023-09-22 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("animals", "0004_auto_20230922_1742"),
    ]

    operations = [
        migrations.AddField(
            model_name="animal",
            name="kind",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="animals.animalkind",
            ),
            preserve_default=False,
        ),
    ]
