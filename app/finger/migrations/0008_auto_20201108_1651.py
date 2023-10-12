# Generated by Django 2.2.16 on 2020-11-08 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finger', '0007_auto_20201108_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='user',
            name='date_parted',
        ),
        migrations.RemoveField(
            model_name='user',
            name='has_key',
        ),
        migrations.RemoveField(
            model_name='user',
            name='honorary_member',
        ),
        migrations.RemoveField(
            model_name='user',
            name='keycard_number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='kth_account',
        ),
        migrations.RemoveField(
            model_name='user',
            name='payed_year',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='user',
            name='support_member',
        ),
        migrations.RemoveField(
            model_name='user',
            name='ths_claimed_ht',
        ),
        migrations.RemoveField(
            model_name='user',
            name='ths_claimed_vt',
        ),
        migrations.RemoveField(
            model_name='user',
            name='ths_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='ths_verified_ht',
        ),
        migrations.RemoveField(
            model_name='user',
            name='ths_verified_vt',
        ),
        migrations.RemoveField(
            model_name='user',
            name='title',
        ),
        migrations.AddField(
            model_name='member',
            name='address',
            field=models.TextField(blank=True, help_text='The members address.', null=True, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='member',
            name='comments',
            field=models.TextField(blank=True, help_text='One or more comments about the member.', null=True, verbose_name='Comments'),
        ),
        migrations.AddField(
            model_name='member',
            name='date_joined',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='date_parted',
            field=models.DateTimeField(blank=True, help_text='The date of when a member left the club.', null=True, verbose_name='Date parted'),
        ),
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.CharField(default=None, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='first_name',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='has_key',
            field=models.BooleanField(default=False, help_text='If the member has a key to the computer hall.', verbose_name='Has a Key'),
        ),
        migrations.AddField(
            model_name='member',
            name='has_signed',
            field=models.BooleanField(default=False, help_text='The user has signed the contract, account access is allowed.', verbose_name='Has signed the contract'),
        ),
        migrations.AddField(
            model_name='member',
            name='honorary_member',
            field=models.BooleanField(default=False, help_text='If the member is a honorary member.', verbose_name='Honorary Member'),
        ),
        migrations.AddField(
            model_name='member',
            name='keycard_number',
            field=models.PositiveIntegerField(blank=True, help_text="The number of KTH's keycard, used by us to grant members access to the clubroom.", null=True, verbose_name='Keycard Number'),
        ),
        migrations.AddField(
            model_name='member',
            name='kth_account',
            field=models.CharField(blank=True, help_text='The KTH accound name, useful when validating THS membership status.', max_length=255, null=True, verbose_name='KTH account'),
        ),
        migrations.AddField(
            model_name='member',
            name='last_name',
            field=models.CharField(default=None, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='phone',
            field=models.CharField(blank=True, help_text='One or several phone numbers to the member.', max_length=255, null=True, verbose_name='Phone'),
        ),
        migrations.AddField(
            model_name='member',
            name='support_member',
            field=models.BooleanField(default=False, help_text='The memeber is an support member, the member has no voting rights.', verbose_name='Support Member'),
        ),
        migrations.AddField(
            model_name='member',
            name='ths_claimed_ht',
            field=models.PositiveSmallIntegerField(blank=True, help_text='The member has claimed to be a THS member for the second half of the specified year.', null=True, verbose_name='THS Claimed Member HT'),
        ),
        migrations.AddField(
            model_name='member',
            name='ths_claimed_vt',
            field=models.PositiveSmallIntegerField(blank=True, help_text='The member has claimed to be a THS member for the fist half of the specified year.', null=True, verbose_name='THS Claimed Member VT'),
        ),
        migrations.AddField(
            model_name='member',
            name='ths_name',
            field=models.CharField(blank=True, help_text='If the member is known by some other name in THS systems, this will override the name when we validates THS membership status.', max_length=255, null=True, verbose_name='THS Name'),
        ),
        migrations.AddField(
            model_name='member',
            name='ths_verified_ht',
            field=models.PositiveSmallIntegerField(blank=True, help_text='The member is verified to be a THS member for the second half of the specified year.', null=True, verbose_name='THS Verified Member HT'),
        ),
        migrations.AddField(
            model_name='member',
            name='ths_verified_vt',
            field=models.PositiveSmallIntegerField(blank=True, help_text='The member is verified to be a THS member for the fist half of the specified year.', null=True, verbose_name='THS Verified Member VT'),
        ),
        migrations.AddField(
            model_name='member',
            name='title',
            field=models.CharField(blank=True, help_text='An optional title to the member.', max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]