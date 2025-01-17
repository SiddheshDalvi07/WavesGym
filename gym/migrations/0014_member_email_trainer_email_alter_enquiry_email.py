# Generated by Django 5.0.6 on 2024-05-25 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0013_enquiry'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.EmailField(default='ind@gmail.com', max_length=100),
        ),
        migrations.AddField(
            model_name='trainer',
            name='email',
            field=models.EmailField(default='ind@gmail.com', max_length=100),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='email',
            field=models.EmailField(default='ind@gmail.com', max_length=100),
        ),
    ]
