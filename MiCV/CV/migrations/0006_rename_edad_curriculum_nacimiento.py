# Generated by Django 3.2.7 on 2021-11-02 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0005_rename_institucion_curriculum_carrera_e_institucion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curriculum',
            old_name='edad',
            new_name='nacimiento',
        ),
    ]
