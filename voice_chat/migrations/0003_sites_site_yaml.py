# Generated by Django 3.1.1 on 2020-10-14 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voice_chat', '0002_sites_tree_script'),
    ]

    operations = [
        migrations.AddField(
            model_name='sites',
            name='site_yaml',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
