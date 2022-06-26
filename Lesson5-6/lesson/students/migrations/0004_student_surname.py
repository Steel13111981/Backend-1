# Generated by Django 4.0.5 on 2022-06-23 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_studentgroup_students_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='surname',
            field=models.CharField(blank=True, choices=[('Petrenko', 'Петренко'), ('Ivanenko', 'Иваненко')], max_length=100, null=True, verbose_name='Фамилия'),
        ),
    ]