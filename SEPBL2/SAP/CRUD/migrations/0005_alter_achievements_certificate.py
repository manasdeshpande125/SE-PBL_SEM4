# Generated by Django 3.2.8 on 2022-04-10 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0004_achievements_certificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievements',
            name='certificate',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
