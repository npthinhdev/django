# Generated by Django 2.1.5 on 2019-01-18 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0002_auto_20190115_1637'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='stripe_supscription_id',
            new_name='stripe_subscription_id',
        ),
    ]
