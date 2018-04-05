# Generated by Django 2.0.3 on 2018-04-03 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recepti', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jela',
            options={'verbose_name_plural': 'Jela'},
        ),
        migrations.AlterModelOptions(
            name='kategorije',
            options={'verbose_name_plural': 'Kategorije'},
        ),
        migrations.AlterModelOptions(
            name='sastojci',
            options={'verbose_name_plural': 'Sastojci'},
        ),
        migrations.AlterModelOptions(
            name='sastojciujelu',
            options={'verbose_name_plural': 'Sastojci u jelu'},
        ),
        migrations.AddField(
            model_name='jela',
            name='je_vegeterijansko',
            field=models.BooleanField(default=False),
        ),
    ]