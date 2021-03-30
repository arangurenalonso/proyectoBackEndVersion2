# Generated by Django 3.1.7 on 2021-03-27 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=255)),
                ('description_short', models.TextField()),
                ('description_long', models.TextField()),
                ('state', models.BooleanField(default=True)),
                ('available', models.BooleanField(default=False)),
                ('price', models.FloatField()),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.FloatField()),
                ('code_paypal', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('unid_number', models.CharField(max_length=200)),
                ('curso_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso')),
            ],
            options={
                'verbose_name': 'Unidad',
                'verbose_name_plural': 'Unidades',
            },
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('week_name', models.CharField(max_length=200)),
                ('unid_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.unit')),
            ],
            options={
                'verbose_name': 'Semana',
                'verbose_name_plural': 'Semanas',
            },
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('curso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.curso')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ShoppingCart',
                'verbose_name_plural': 'ShoppingCarts',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('curso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.curso')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.order')),
            ],
            options={
                'verbose_name': 'OrderDetail',
                'verbose_name_plural': 'OrderDetails',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Lesson_name', models.CharField(max_length=200)),
                ('week_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.week')),
            ],
            options={
                'verbose_name': 'Leccion',
                'verbose_name_plural': 'Lecciones',
            },
        ),
        migrations.CreateModel(
            name='Inicio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('starting_date', models.DateField(max_length=200)),
                ('curso_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso')),
            ],
            options={
                'verbose_name': 'Inicio',
                'verbose_name_plural': 'Inicios',
            },
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('frequency', models.CharField(max_length=200)),
                ('schedule', models.CharField(max_length=200)),
                ('inicio_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.inicio')),
            ],
            options={
                'verbose_name': 'Horario',
                'verbose_name_plural': 'Horarios',
            },
        ),
    ]
