# Generated by Django 3.1.1 on 2021-01-17 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voice_chat', '0007_auto_20210117_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='data',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
