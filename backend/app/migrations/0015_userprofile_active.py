# Generated by Django 4.2.3 on 2023-07-30 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_message_sender'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
