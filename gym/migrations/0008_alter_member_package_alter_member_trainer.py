# Generated by Django 5.0.6 on 2024-05-24 08:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0007_auto_20220721_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='package',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.package'),
        ),
        migrations.AlterField(
            model_name='member',
            name='trainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.trainer'),
        ),
    ]
