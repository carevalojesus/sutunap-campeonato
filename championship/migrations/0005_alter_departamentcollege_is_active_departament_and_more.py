# Generated by Django 4.2.6 on 2023-11-01 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('championship', '0004_remove_phase_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamentcollege',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='Departament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('short_name', models.CharField(max_length=10)),
                ('is_active', models.BooleanField(default=True)),
                ('departament_college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='championship.departamentcollege')),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='departament',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='championship.departament'),
        ),
    ]
