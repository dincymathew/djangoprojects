# Generated by Django 4.2.5 on 2023-12-16 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='User',
            new_name='user',
        ),
    ]
