# Generated by Django 4.2.4 on 2023-08-22 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('location', models.CharField(max_length=50)),
                ('type', models.TextField(choices=[('IT', 'IT'), ('Non IT', 'Non IT'), ('Mobile Phone', 'Mobile Phone')])),
                ('date_time', models.DateTimeField(auto_now=True)),
                ('about', models.TextField(max_length=500)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
