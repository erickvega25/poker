# Generated by Django 3.2.9 on 2021-12-10 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corePoker', '0011_player_acambiado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='aCambiado',
            new_name='haCambiado',
        ),
    ]