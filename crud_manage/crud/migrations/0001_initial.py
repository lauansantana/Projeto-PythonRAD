# Generated by Django 4.2.1 on 2023-06-01 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=12)),
                ('nome', models.CharField(max_length=70)),
                ('email', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=150)),
                ('telefone', models.CharField(max_length=11)),
            ],
        ),
    ]
