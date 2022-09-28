# Generated by Django 4.1 on 2022-09-28 19:10

import cpf_field.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudante', '0002_alter_alunos_matricula'),
    ]

    operations = [
        migrations.CreateModel(
            name='Egresso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', cpf_field.models.CPFField(max_length=14, verbose_name='cpf')),
                ('nome_egresso', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_matricula', models.DateTimeField()),
                ('usuario_responsavel', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_pai', models.CharField(max_length=100)),
                ('nome_mae', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='alunos',
            name='cpf',
            field=cpf_field.models.CPFField(max_length=14, verbose_name='cpf'),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='data_nascimento',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='email',
            field=models.EmailField(max_length=130),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='estado_civil',
            field=models.CharField(blank=True, choices=[('S', 'Solteiro'), ('C', 'Casado'), ('V', 'Viúvo'), ('H', 'Separado'), ('D', 'Divorciado'), ('U', 'União Estável')], max_length=1),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='matricula',
            field=models.CharField(max_length=15, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='nome',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='senha',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='sexo',
            field=models.CharField(blank=True, choices=[('H', 'Homem Cis'), ('M', 'Mulher Cis'), ('K', 'Homem Trans'), ('W', 'Mulher Trans')], max_length=1),
        ),
    ]
