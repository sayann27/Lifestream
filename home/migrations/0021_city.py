# Generated by Django 4.1.7 on 2023-04-14 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_remove_donor_manager_id_remove_donor_staff_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_ID', models.IntegerField()),
                ('name', models.CharField(max_length=122)),
            ],
        ),
    ]
