# Generated by Django 4.0.5 on 2022-07-05 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_tasks', '0002_alter_status_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='title',
            field=models.CharField(max_length=100, verbose_name='наименование'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_tasks.status', verbose_name='статус'),
        ),
    ]
