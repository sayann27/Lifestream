# Generated by Django 4.1.7 on 2023-04-08 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_receiving'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blood_group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hosp_email', models.CharField(blank=True, max_length=122, null=True)),
                ('Apos', models.IntegerField(default=0)),
                ('Aneg', models.IntegerField(default=0)),
                ('Bpos', models.IntegerField(default=0)),
                ('Bneg', models.IntegerField(default=0)),
                ('ABpos', models.IntegerField(default=0)),
                ('ABneg', models.IntegerField(default=0)),
                ('Opos', models.IntegerField(default=0)),
                ('Oneg', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='bg_needed',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='quantity_needed',
        ),
    ]
