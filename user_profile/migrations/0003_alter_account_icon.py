# Generated by Django 4.2.3 on 2023-07-05 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='icon',
            field=models.ImageField(upload_to='icons'),
        ),
    ]
