# Generated by Django 2.2.1 on 2019-12-19 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('REZERVAPP', '0005_auto_20191219_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='requests',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='REZERVAPP.Request'),
        ),
    ]
