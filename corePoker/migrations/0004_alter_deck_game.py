# Generated by Django 3.2.9 on 2021-11-29 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corePoker', '0003_card_positionindeck'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='game',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='corePoker.game'),
        ),
    ]
