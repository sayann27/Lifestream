# Generated by Django 4.1.7 on 2023-03-28 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_hospital_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='cover_image',
            field=models.BinaryField(null=True),
        ),
    ]