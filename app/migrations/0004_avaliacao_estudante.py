# Generated by Django 5.1.3 on 2024-12-03 19:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_disciplina_estudante'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacao',
            name='estudante',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.estudante', verbose_name='Pessoa'),
        ),
    ]
