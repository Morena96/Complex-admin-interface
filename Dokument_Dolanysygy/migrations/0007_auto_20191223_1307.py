# Generated by Django 3.0.1 on 2019-12-23 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dokument_Dolanysygy', '0006_remove_file_welaýaty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='döredilen_senesi',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='üýgedilen_senesi',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
