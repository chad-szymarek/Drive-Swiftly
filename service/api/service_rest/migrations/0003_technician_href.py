# Generated by Django 4.0.3 on 2022-05-09 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0002_automobilevo'),
    ]

    operations = [
        migrations.AddField(
            model_name='technician',
            name='href',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]