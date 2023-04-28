# Generated by Django 4.1.7 on 2023-04-27 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market_analysis', '0010_alter_walmartsales_isholiday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walmartsales',
            name='isHoliday',
            field=models.BooleanField(choices=[('0', 'Workingday'), ('1', 'Holiday')], max_length=1, verbose_name='Holiday'),
        ),
    ]
