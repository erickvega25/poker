# Generated by Django 3.2.9 on 2021-12-10 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corePoker', '0008_game_winner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='lastname',
            field=models.CharField(default='', max_length=255),
        ),
    ]
