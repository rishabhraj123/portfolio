# Generated by Django 2.2.1 on 2019-06-01 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='image',
            new_name='image_field',
        ),
    ]
