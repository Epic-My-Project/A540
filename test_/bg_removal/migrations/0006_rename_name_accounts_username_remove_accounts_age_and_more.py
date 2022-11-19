# Generated by Django 4.1.2 on 2022-11-19 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bg_removal', '0005_accounts_age_accounts_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accounts',
            old_name='name',
            new_name='userName',
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='age',
        ),
        migrations.AddField(
            model_name='accounts',
            name='userAge',
            field=models.CharField(default='나이', max_length=20),
        ),
    ]