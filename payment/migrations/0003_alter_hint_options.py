# Generated by Django 4.2.16 on 2024-10-01 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_paymentmethod_image_paymentmethod_link'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hint',
            options={'verbose_name': 'Підказки', 'verbose_name_plural': 'Підказки'},
        ),
    ]
