# Generated by Django 4.2.4 on 2023-08-28 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0002_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.CharField(blank=True, choices=[('Manager', 'Manager'), ('Software Developer', 'Software Developer'), ('Labour', 'Labour')], max_length=50),
        ),
    ]
