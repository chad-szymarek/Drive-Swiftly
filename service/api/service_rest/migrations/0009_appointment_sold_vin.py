# Generated by Django 4.0.3 on 2022-05-10 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0008_alter_technician_employee_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='sold_vin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='service_rest.automobilevo'),
        ),
    ]
