# Generated by Django 3.0.9 on 2020-09-24 08:41

from django.db import migrations

import gnosis.eth.django.models


class Migration(migrations.Migration):

    dependencies = [
        ("history", "0022_auto_20200903_1045"),
    ]

    operations = [
        migrations.AlterField(
            model_name="multisigconfirmation",
            name="signature",
            field=gnosis.eth.django.models.HexField(
                default=None, max_length=2000, null=True
            ),
        ),
    ]
