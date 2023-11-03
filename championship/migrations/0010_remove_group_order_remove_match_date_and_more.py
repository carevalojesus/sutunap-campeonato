# Generated by Django 4.2.6 on 2023-11-02 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('championship', '0009_match_group_match_phase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='order',
        ),
        migrations.RemoveField(
            model_name='match',
            name='date',
        ),
        migrations.RemoveField(
            model_name='match',
            name='edition',
        ),
        migrations.RemoveField(
            model_name='match',
            name='group',
        ),
        migrations.RemoveField(
            model_name='match',
            name='phase',
        ),
        migrations.CreateModel(
            name='MatchDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='championship.group')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='match_day',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='championship.matchday'),
        ),
    ]
