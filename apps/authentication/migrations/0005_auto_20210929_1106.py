# Generated by Django 3.1.12 on 2021-09-29 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_ssotoken'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='loginconfirmsetting',
            options={'verbose_name': 'Login Confirm'},
        ),
    ]
