# Generated by Django 3.2.9 on 2021-12-10 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corePoker', '0007_auto_20211210_0832'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='winner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='winner', to='corePoker.player'),
        ),
    ]
