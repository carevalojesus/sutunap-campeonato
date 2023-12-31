# Generated by Django 4.2.6 on 2023-11-02 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('championship', '0008_team_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='championship.group'),
        ),
        migrations.AddField(
            model_name='match',
            name='phase',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='championship.phase'),
        ),
    ]
