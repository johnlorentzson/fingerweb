# Generated by Django 2.1.4 on 2019-01-03 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_service_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceuser',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
