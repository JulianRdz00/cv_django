# Generated by Django 3.2.7 on 2021-10-28 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0004_curriculum_hobbies'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curriculum',
            old_name='institucion',
            new_name='carrera_e_institucion',
        ),
    ]
