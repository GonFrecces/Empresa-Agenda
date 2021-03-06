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
            name='Contacto',
            fields=[
                ('IdContacto', models.AutoField(primary_key=True, serialize=False, verbose_name='IdContacto')),
                ('Nombre_contacto', models.TextField(max_length=255)),
                ('Apellidos', models.TextField(max_length=255)),
                ('Telefono', models.TextField(max_length=8)),
                ('Email', models.EmailField(max_length=50)),
                ('Direccion', models.TextField(max_length=150)),
                ('Comuna', models.ForeignKey(db_column='Nombre', on_delete=django.db.models.deletion.CASCADE, to='appComuna.Comuna')),
            ],
        ),
    ]
