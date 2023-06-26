# Generated by Django 4.2.2 on 2023-06-26 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0005_auto_20230626_1752"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="shop.category"
            ),
        ),
    ]
