# Generated by Django 4.2.4 on 2023-08-23 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0003_alter_company_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='about',
            field=models.TextField(max_length=500),
        ),
    ]
