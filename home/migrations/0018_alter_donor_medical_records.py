# Generated by Django 4.1.7 on 2023-04-10 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_blood_group_abneg_alter_blood_group_abpos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='medical_records',
            field=models.TextField(blank=True, default='None', null=True),
        ),
    ]