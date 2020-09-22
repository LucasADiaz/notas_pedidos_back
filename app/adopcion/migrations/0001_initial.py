# Generated by Django 3.1 on 2020-09-15 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('telefono', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254)),
                ('domicilio', models.TextField()),
            ],
        ),
    ]
