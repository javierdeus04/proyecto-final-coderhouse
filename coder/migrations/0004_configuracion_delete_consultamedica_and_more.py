# Generated by Django 4.0.4 on 2022-10-29 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coder', '0003_consultamedica_delete_consultasmedicas_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empresa', models.CharField(max_length=14)),
                ('construido_por', models.CharField(max_length=30)),
                ('titulo_principal', models.CharField(default='', max_length=30)),
                ('subtitulo_principal', models.CharField(default='', max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('fecha_de_nacimiento', models.DateField()),
                ('numero_ci', models.IntegerField()),
                ('numero_cel', models.IntegerField()),
                ('motivo_de_consulta', models.CharField(max_length=30)),
                ('numero', models.IntegerField()),
                ('capacidad', models.IntegerField()),
                ('is_reserved', models.BooleanField(default=False)),
                ('fecha_y_hora', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='ConsultaMedica',
        ),
        migrations.DeleteModel(
            name='Funcionario',
        ),
        migrations.DeleteModel(
            name='Paciente',
        ),
    ]
