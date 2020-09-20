# Generated by Django 3.1.1 on 2020-09-19 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Voluntary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80, verbose_name='Nome')),
                ('last_name', models.CharField(max_length=100, verbose_name='Sobrenome')),
                ('neighborhood', models.CharField(max_length=80, verbose_name='Bairro')),
                ('city', models.CharField(max_length=100, verbose_name='Cidade')),
            ],
            options={
                'verbose_name': 'Voluntário',
                'verbose_name_plural': 'Voluntários',
                'ordering': ['id', 'first_name', 'last_name'],
            },
        ),
    ]