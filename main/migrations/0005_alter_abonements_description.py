# Generated by Django 4.0.4 on 2022-05-04 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_abonements_clubs_equipments_grouptraining_partners'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abonements',
            name='description',
            field=models.CharField(max_length=200, verbose_name='Описание'),
        ),
    ]
