# Generated by Django 4.2.1 on 2023-06-12 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='id',
            new_name='_id',
        ),
    ]