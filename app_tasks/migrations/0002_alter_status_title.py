# Generated by Django 4.0.5 on 2022-07-05 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='title',
            field=models.CharField(default='в работе', max_length=100, verbose_name='наименование'),
        ),
    ]
