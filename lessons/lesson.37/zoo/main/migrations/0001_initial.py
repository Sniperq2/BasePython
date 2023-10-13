# Generated by Django 3.2 on 2023-10-13 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('age', models.PositiveSmallIntegerField(null=True)),
                ('desc', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AnimalKind',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('desc', models.TextField(blank=True)),
                ('max_age', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AnimalDetail',
            fields=[
                ('animal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.animal')),
                ('biography', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AnimalFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('animal', models.ManyToManyField(to='main.Animal')),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='kind',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.animalkind'),
        ),
    ]
