# Generated by Django 5.0.6 on 2024-05-25 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0015_remove_member_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.EmailField(default='ind@gmail.com', max_length=100),
        ),
    ]