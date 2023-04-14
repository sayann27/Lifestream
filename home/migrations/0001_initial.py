# Generated by Django 4.1.7 on 2023-03-26 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('dob', models.DateField()),
                ('phone', models.CharField(max_length=13)),
                ('bg', models.CharField(max_length=3)),
                ('user_type', models.CharField(max_length=20)),
                ('addline1', models.TextField()),
                ('addline2', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.IntegerField()),
                ('pwd', models.CharField(max_length=16)),
            ],
        ),
    ]
