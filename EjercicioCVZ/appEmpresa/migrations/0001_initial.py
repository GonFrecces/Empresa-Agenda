# Generated by Django 3.0.14 on 2022-05-01 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appComuna', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('IdEmpresa', models.AutoField(primary_key=True, serialize=False, verbose_name='IdContacto')),
                ('Nombre_empresa', models.CharField(max_length=255)),
                ('Rut', models.CharField(max_length=10)),
                ('Direccion', models.CharField(max_length=100)),
                ('Comuna', models.ForeignKey(db_column='Nombre', on_delete=django.db.models.deletion.CASCADE, to='appComuna.Comuna')),
            ],
        ),
    ]
