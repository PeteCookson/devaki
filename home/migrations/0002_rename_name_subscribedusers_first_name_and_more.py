# Generated by Django 4.2.3 on 2023-07-17 20:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscribedusers',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='subscribedusers',
            name='last_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]