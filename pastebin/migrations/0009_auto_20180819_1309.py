# Generated by Django 2.0 on 2018-08-19 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastebin', '0008_auto_20180819_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paste',
            name='url',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
