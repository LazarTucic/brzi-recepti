# Generated by Django 2.0.3 on 2018-04-05 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recepti', '0006_remove_jela_svidja_mi_se'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jela',
            old_name='kategorija_id',
            new_name='kategorija',
        ),
        migrations.RenameField(
            model_name='jela',
            old_name='opis',
            new_name='sastojci',
        ),
        migrations.RenameField(
            model_name='sastojciujelu',
            old_name='jelo_id',
            new_name='jelo',
        ),
        migrations.AlterField(
            model_name='jela',
            name='slika',
            field=models.FileField(upload_to=''),
        ),
    ]
