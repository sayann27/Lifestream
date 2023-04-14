# Generated by Django 4.1.7 on 2023-03-28 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_donor_receiver'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=13)),
                ('addline1', models.TextField()),
                ('addline2', models.TextField(blank=True, null=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.IntegerField()),
                ('pwd', models.CharField(max_length=16)),
                ('quantity_needed', models.IntegerField()),
                ('bg_needed', models.CharField(max_length=3)),
            ],
        ),
    ]
