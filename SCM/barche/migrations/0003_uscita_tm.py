# Generated by Django 4.2.1 on 2023-10-01 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barche', '0002_uscita_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='uscita',
            name='tm',
            field=models.CharField(choices=[('terra', 'Terra'), ('mare', 'Mare')], default='terra', max_length=100),
        ),
    ]