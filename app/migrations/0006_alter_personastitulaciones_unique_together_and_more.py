# Generated by Django 4.2.5 on 2023-10-08 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_barrios_nombre_alter_campus_nombre_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='personastitulaciones',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='barrios',
            name='nombre',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='campus',
            name='nombre',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='carreras',
            name='nombre',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='ciudades',
            name='nombre',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='facultades',
            name='nombre',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='generos',
            name='nombre',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='lugares',
            name='barrio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.barrios'),
        ),
        migrations.AlterField(
            model_name='lugares',
            name='ciudad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.ciudades'),
        ),
        migrations.AlterField(
            model_name='lugares',
            name='pais',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.paises'),
        ),
        migrations.AlterField(
            model_name='lugares',
            name='provincia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.provincias'),
        ),
        migrations.AlterField(
            model_name='paises',
            name='nombre',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='personas',
            name='apellido',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personas',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personas',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='personas',
            name='genero',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.generos'),
        ),
        migrations.AlterField(
            model_name='personas',
            name='lugar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.lugares'),
        ),
        migrations.AlterField(
            model_name='personas',
            name='nombre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personas',
            name='personal_id',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='personastitulaciones',
            name='persona',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.personas'),
        ),
        migrations.AlterField(
            model_name='personastitulaciones',
            name='tipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.tipospersona'),
        ),
        migrations.AlterField(
            model_name='personastitulaciones',
            name='titulacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.titulaciones'),
        ),
        migrations.AlterField(
            model_name='provincias',
            name='nombre',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='tipospersona',
            name='nombre',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='titulaciones',
            name='campus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.campus'),
        ),
        migrations.AlterField(
            model_name='titulaciones',
            name='carrera',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.carreras'),
        ),
        migrations.AlterField(
            model_name='titulaciones',
            name='facultad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.facultades'),
        ),
        migrations.AlterField(
            model_name='titulaciones',
            name='universidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.universidades'),
        ),
        migrations.AlterField(
            model_name='universidades',
            name='nombre',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='titulaciones',
            unique_together={('carrera', 'facultad', 'universidad', 'campus')},
        ),
    ]
