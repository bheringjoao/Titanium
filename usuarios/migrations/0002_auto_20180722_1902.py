# Generated by Django 2.0.7 on 2018-07-22 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characters',
            name='vocacao',
            field=models.TextField(choices=[('D', 'Druid'), ('K', 'Knight'), ('S', 'Sorcerer'), ('P', 'Paladin'), ('ED', 'Elder Druid'), ('EK', 'Elite Knight'), ('MS', 'Master Sorcerer'), ('RP', 'Royal Paladin')]),
        ),
    ]