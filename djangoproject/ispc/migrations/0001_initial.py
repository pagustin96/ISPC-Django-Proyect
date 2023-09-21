# Generated by Django 4.2.2 on 2023-08-03 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barrios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True, unique=True)),
            ],
            options={
                'db_table': 'barrios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True, unique=True)),
            ],
            options={
                'db_table': 'campus',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Carreras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True, unique=True)),
            ],
            options={
                'db_table': 'carreras',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ciudades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True, unique=True)),
            ],
            options={
                'db_table': 'ciudades',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Facultades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True, unique=True)),
            ],
            options={
                'db_table': 'facultades',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Generos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True, unique=True)),
            ],
            options={
                'db_table': 'generos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lugares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'lugares',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Paises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True, unique=True)),
            ],
            options={
                'db_table': 'paises',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('apellido', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('personal_id', models.CharField(blank=True, max_length=50, null=True, unique=True)),
            ],
            options={
                'db_table': 'personas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PersonasTitulaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'personas_titulaciones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Provincias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True, unique=True)),
            ],
            options={
                'db_table': 'provincias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TiposPersona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True, unique=True)),
            ],
            options={
                'db_table': 'tipos_persona',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Titulaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'titulaciones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Universidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True, unique=True)),
            ],
            options={
                'db_table': 'universidades',
                'managed': False,
            },
        ),
    ]
