# Generated by Django 3.0.1 on 2019-12-25 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dokument_Dolanysygy', '0009_auto_20191225_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='hasabat',
            name='ady_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='hasabat',
            name='ady_tr',
            field=models.CharField(max_length=200, null=True),
        ),
    ]