# Generated by Django 4.0.2 on 2022-02-03 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grupos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('Sobrenome', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('Naturalidade', models.CharField(max_length=100)),
                ('hobby', models.CharField(max_length=100)),
            ],
        ),
    ]
