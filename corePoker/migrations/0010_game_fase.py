# Generated by Django 3.2.9 on 2021-12-10 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corePoker', '0009_alter_player_lastname'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='fase',
            field=models.IntegerField(default=0),
        ),
    ]
