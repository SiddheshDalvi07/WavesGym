# Generated by Django 5.0.6 on 2024-05-25 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0014_member_email_trainer_email_alter_enquiry_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='email',
        ),
    ]
