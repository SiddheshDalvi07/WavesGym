# Generated by Django 5.0.6 on 2024-05-25 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0012_alter_userprofile_is_member_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=40)),
                ('lname', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('category', models.CharField(choices=[(1, 'Free 1 Day Pass'), (2, 'Complimentary Personal Training Session'), (3, 'Complimentary Zumba Class'), (4, 'Complimentary Spin Class / Indoor Cycling Class'), (5, 'Complimentary Power Yoga Class'), (6, 'Complimentary Kickboxing Class')], max_length=60)),
            ],
        ),
    ]
