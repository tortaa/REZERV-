# Generated by Django 2.2.1 on 2019-12-20 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('REZERVAPP', '0008_auto_20191220_2344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='best',
            name='profile_id',
        ),
        migrations.AddField(
            model_name='best',
            name='profile_id',
            field=models.ManyToManyField(to='REZERVAPP.profile'),
        ),
    ]