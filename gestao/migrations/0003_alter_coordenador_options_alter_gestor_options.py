# Generated by Django 4.1 on 2022-12-13 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0002_alter_professor_options_alter_coordenador_nome_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coordenador',
            options={'permissions': (('views_coordenador', 'pode ver views do grupo coordenador'),)},
        ),
        migrations.AlterModelOptions(
            name='gestor',
            options={'permissions': (('views_gestor', 'pode ver views do grupo gestor'),)},
        ),
    ]
