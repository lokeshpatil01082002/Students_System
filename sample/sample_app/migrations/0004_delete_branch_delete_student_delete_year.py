# Generated by Django 4.1.3 on 2022-12-04 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sample_app', '0003_student'),
    ]

    operations = [
        migrations.DeleteModel(
            name='branch',
        ),
        migrations.DeleteModel(
            name='student',
        ),
        migrations.DeleteModel(
            name='year',
        ),
    ]
