# Generated by Django 5.0.6 on 2024-05-24 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0011_alter_userprofile_is_member_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='is_member',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_trainer',
            field=models.BooleanField(default=False),
        ),
    ]
