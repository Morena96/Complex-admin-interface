# Generated by Django 3.0.1 on 2019-12-26 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dokument_Dolanysygy', '0010_auto_20191225_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ulanyjy',
            name='edarasy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Dokument_Dolanysygy.Edaralar'),
            preserve_default=False,
        ),
    ]
