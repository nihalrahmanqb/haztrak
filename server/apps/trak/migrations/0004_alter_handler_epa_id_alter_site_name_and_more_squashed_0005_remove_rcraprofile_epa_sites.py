# Generated by Django 4.1.6 on 2023-02-08 17:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('trak', '0004_alter_handler_epa_id_alter_site_name_and_more'), ('trak', '0005_remove_rcraprofile_epa_sites')]

    dependencies = [
        ('trak', '0003_alter_manifest_mtn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='handler',
            name='epa_id',
            field=models.CharField(max_length=25, unique=True, verbose_name='EPA Id number'),
        ),
        migrations.AlterField(
            model_name='site',
            name='name',
            field=models.CharField(max_length=200, validators=[django.core.validators.MinValueValidator(2, 'site aliases must be longer than 2 characters')], verbose_name='site Alias'),
        ),
        migrations.AlterField(
            model_name='transporter',
            name='order',
            field=models.PositiveIntegerField(),
        ),
        migrations.RemoveField(
            model_name='rcraprofile',
            name='epa_sites',
        ),
    ]
