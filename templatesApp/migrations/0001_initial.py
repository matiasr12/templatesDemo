# Generated by Django 4.1.3 on 2022-11-27 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('edad', models.CharField(max_length=40)),
                ('cargo', models.CharField(max_length=40)),
                ('fechaInicio', models.DateField(max_length=40)),
                ('fechatermino', models.DateField(max_length=10)),
                ('saldo', models.CharField(max_length=40)),
                ('casado', models.CharField(max_length=40)),
            ],
        ),
    ]
