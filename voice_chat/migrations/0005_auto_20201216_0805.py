# Generated by Django 3.1.1 on 2020-12-16 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voice_chat', '0004_config'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='data',
            field=models.JSONField(blank=True, default=None, null=True),
        ),
    ]
