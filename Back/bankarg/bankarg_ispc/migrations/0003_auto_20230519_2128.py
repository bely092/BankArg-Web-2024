# Generated by Django 3.2 on 2023-05-20 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bankarg_ispc', '0002_auto_20230519_2043'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_empleado',
            fields=[
                ('id_tipo_empleado', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_empleado', models.TextField(max_length=150)),
            ],
            options={
                'verbose_name': 'Tipo_Empleado',
                'verbose_name_plural': 'Tipos_Empleados',
                'db_table': 'Tipo_Empleado',
            },
        ),
        migrations.CreateModel(
            name='Tipo_estado_cuenta',
            fields=[
                ('id_tipo_estado_cuenta', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_estado_cuenta', models.TextField(max_length=150)),
            ],
            options={
                'verbose_name': 'Tipo_estado_cuenta',
                'verbose_name_plural': 'Tipos_estado_cuentas',
                'db_table': 'Tipo_estado_cuenta',
            },
        ),
        migrations.CreateModel(
            name='Tipo_estado_empleado',
            fields=[
                ('id_tipo_estado_empleado', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_estado_empleado', models.TextField(max_length=150)),
            ],
            options={
                'verbose_name': 'Tipo_estado_empleado',
                'verbose_name_plural': 'Tipos_estado_empleados',
                'db_table': 'Tipo_estado_empleado',
            },
        ),
        migrations.AlterModelOptions(
            name='clientes',
            options={'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterModelTable(
            name='clientes',
            table='Clientes',
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='bankarg_ispc.persona')),
                ('id_empleado', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_ingreso', models.DateTimeField()),
                ('sueldo', models.DecimalField(decimal_places=2, max_digits=15)),
                ('id_tipo_empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.tipo_empleado')),
                ('id_tipo_estado_empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.tipo_estado_empleado')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'db_table': 'Empleado',
            },
            bases=('bankarg_ispc.persona',),
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id_cuenta', models.AutoField(primary_key=True, serialize=False)),
                ('monto', models.IntegerField()),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('cbu', models.CharField(max_length=75)),
                ('alias', models.TextField(max_length=150)),
                ('password', models.TextField(max_length=250)),
                ('credito', models.BooleanField(default=True)),
                ('debito', models.BooleanField(default=True)),
                ('id_tipo_estado_cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.tipo_estado_cuenta')),
            ],
            options={
                'verbose_name': 'Cuenta',
                'verbose_name_plural': 'Cuentas',
                'db_table': 'Cuenta',
            },
        ),
    ]
