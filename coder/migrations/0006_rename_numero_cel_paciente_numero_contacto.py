# Generated by Django 4.0.4 on 2022-10-29 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coder', '0005_paciente_delete_configuracion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='numero_cel',
            new_name='numero_contacto',
        ),
    ]
