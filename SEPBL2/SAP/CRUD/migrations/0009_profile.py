# Generated by Django 3.2.8 on 2022-04-29 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0008_auto_20220426_2102'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=200, null=True)),
                ('div', models.CharField(max_length=200, null=True)),
                ('dept', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
