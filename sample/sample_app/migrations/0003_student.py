# Generated by Django 4.1.3 on 2022-12-04 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sample_app', '0002_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sample_app.year')),
            ],
        ),
    ]
