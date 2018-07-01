# Generated by Django 2.0.6 on 2018-06-30 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finger', '0003_auto_20180628_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='payed_year',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='ths_claimed_ht',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='ths_claimed_vt',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='ths_verified_ht',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='ths_verified_vt',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]