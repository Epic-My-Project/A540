# Generated by Django 4.1.2 on 2022-11-16 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bg_removal', '0002_accounts_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Accounts',
        ),
    ]
