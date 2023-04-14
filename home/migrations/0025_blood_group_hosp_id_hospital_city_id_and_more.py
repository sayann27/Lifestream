# Generated by Django 4.1.7 on 2023-04-14 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_alter_donor_city_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='blood_group',
            name='hosp_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.hospital'),
        ),
        migrations.AddField(
            model_name='hospital',
            name='city_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.city'),
        ),
        migrations.AlterField(
            model_name='receiver',
            name='city_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.city'),
        ),
    ]
