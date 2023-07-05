# Generated by Django 4.2.3 on 2023-07-04 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=50)),
                ('bank', models.CharField(choices=[('NU', 'Nubank'), ('CE', 'Caixa Economica')], max_length=2)),
                ('bank_type', models.CharField(choices=[('pp', 'Physical Person'), ('jp', 'Juridical Person')], max_length=2)),
                ('value', models.IntegerField()),
                ('icon', models.ImageField(upload_to='icones')),
            ],
        ),
    ]