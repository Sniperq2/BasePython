# Generated by Django 4.2.5 on 2023-09-22 17:42

from django.db import migrations


def create_default_animal_kind(apps, schema_editor):
    AnimalKind = apps.get_model("animals", "AnimalKind")
    AnimalKind.objects.get_or_create(
        name="default",
        description="Default animal kind (category)",
    )


class Migration(migrations.Migration):
    dependencies = [
        ("animals", "0003_animalkind"),
    ]

    operations = [
        migrations.RunPython(
            code=create_default_animal_kind,
        )
    ]
