# Generated by Django 4.2.6 on 2023-11-01 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('championship', '0003_rename_edition_match_edition_phase_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phase',
            name='type',
        ),
    ]
