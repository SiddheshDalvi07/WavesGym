# Generated by Django 3.0.5 on 2022-07-18 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0002_auto_20220718_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]