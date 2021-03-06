# Generated by Django 2.0 on 2018-08-27 10:57

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastebin', '0013_auto_20180822_0756'),
    ]

    operations = [
        migrations.AddField(
            model_name='paste',
            name='expiration_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='paste_logged_in',
            name='expiration_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paste',
            name='content',
            field=ckeditor.fields.RichTextField(max_length=1000000),
        ),
    ]
