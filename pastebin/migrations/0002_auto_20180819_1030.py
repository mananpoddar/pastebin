# Generated by Django 2.0 on 2018-08-19 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastebin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paste',
            name='id',
        ),
        migrations.AlterField(
            model_name='paste',
            name='url',
            field=models.CharField(max_length=32, primary_key=True, serialize=False),
        ),
    ]
