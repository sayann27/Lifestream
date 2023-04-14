# Generated by Django 4.1.7 on 2023-03-28 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_hospital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='bg_needed',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='quantity_needed',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]