# Generated by Django 4.2.6 on 2023-11-02 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('championship', '0006_alter_team_short_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
