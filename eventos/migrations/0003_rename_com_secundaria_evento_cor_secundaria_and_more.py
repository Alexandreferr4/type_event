# Generated by Django 4.2 on 2023-04-12 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_evento_criador'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='com_secundaria',
            new_name='cor_secundaria',
        ),
        migrations.RenameField(
            model_name='evento',
            old_name='date_inicio',
            new_name='data_inicio',
        ),
        migrations.RenameField(
            model_name='evento',
            old_name='date_termino',
            new_name='data_termino',
        ),
    ]
